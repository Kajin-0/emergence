import json,time,platform,numpy as np,torch
from torch import nn
P=31; H=128; PRE=300; CUT=600; END=2500; TH=.90
torch.set_num_threads(2)
x=torch.arange(P).repeat_interleave(P); y=torch.arange(P).repeat(P); labels=(x+y)%P; dif=(y-x)%P
X=torch.cat([nn.functional.one_hot(x,P),nn.functional.one_hot(y,P)],1).float()
class Model(nn.Module):
 def __init__(self):
  super().__init__(); self.input=nn.Linear(2*P,H); self.out=nn.Linear(H,P)
 def features(self,x): return self.input(x).square()
 def forward(self,x): return self.out(self.features(x))
def accuracy(logits,fam):
 good=logits.argmax(1)==labels
 return np.array([float(good[dif==d].float().mean()) for d in fam])
def metrics(s,t):
 s=np.array(s); t=np.array(t,dtype=bool); p=s>=TH; tp=int((p&t).sum()); fp=int((p&~t).sum()); fn=int((~p&t).sum()); tn=int((~p&~t).sum()); a=s[t]; b=s[~t]
 return dict(tp=tp,fp=fp,fn=fn,tn=tn,accuracy=(tp+tn)/len(t) if len(t) else None,precision=tp/(tp+fp) if tp+fp else None,recall=tp/(tp+fn) if tp+fn else None,auc=float(((a[:,None]>b[None,:])+.5*(a[:,None]==b[None,:])).mean()) if len(a) and len(b) else None)
@torch.no_grad()
def snap(model,train,fam,probe=False):
 h=model.features(X); logits=model.out(h); r=dict(raw=accuracy(logits,fam).tolist(),train_accuracy=float((logits[train].argmax(1)==labels[train]).float().mean()),train_loss=float(nn.functional.cross_entropy(logits[train],labels[train])))
 if probe:
  ht=h[train].double(); mean=ht.mean(0); scale=(ht-mean).square().mean(0).sqrt().clamp_min(1e-6); z=(h.double()-mean)/scale; zt=z[train]; target=nn.functional.one_hot(labels[train],P).double(); avg=target.mean(0)
  coef=torch.linalg.solve(zt.T@zt+torch.eye(H,dtype=torch.double),zt.T@(target-avg)); r['ridge']=accuracy(z@coef+avg,fam).tolist()
  proj=torch.zeros(P,P); proj.index_add_(0,labels,logits); proj/=P; r['restricted']=accuracy(proj[labels],fam).tolist()
  hc=h-h.mean(0); hp=torch.zeros(P,H); hp.index_add_(0,labels,hc); hp/=P; r['sum_energy']=float(hp[labels].square().sum()/hc.square().sum())
 return r
def main():
 start=time.monotonic(); pooled={k:[] for k in ('ridge','persistence','extrapolation','restricted')}; truthpool=[]
 print(json.dumps(dict(torch=torch.__version__,numpy=np.__version__,python=platform.python_version(),threads=2,p=P,hidden=H,cutoff=CUT,horizon=END)),flush=True)
 for seed in (0,1,2):
  torch.manual_seed(seed); perm=np.random.default_rng(seed).permutation(P); fam=sorted(map(int,perm[20:])); train=torch.isin(dif,torch.tensor(perm[:20])); model=Model(); opt=torch.optim.AdamW(model.parameters(),lr=.003,weight_decay=1.); xt=X[train]; yt=labels[train]
  for step in range(1,END+1):
   opt.zero_grad(); loss=nn.functional.cross_entropy(model(xt),yt); loss.backward(); opt.step()
   if step==PRE: prev=snap(model,train,fam)
   if step==CUT:
    early=snap(model,train,fam,True); raw=np.array(early['raw']); elig=raw<TH; scores=dict(ridge=np.array(early['ridge']),persistence=raw,extrapolation=np.clip(raw+(raw-np.array(prev['raw']))*(END-CUT)/(CUT-PRE),0,1),restricted=np.array(early['restricted']))
    print(json.dumps(dict(seed=seed,stage='cutoff',families=fam,eligible=elig.tolist(),previous=prev,early=early,scores={k:v.tolist() for k,v in scores.items()})),flush=True)
   if step==END: end=snap(model,train,fam)
  truth=np.array(end['raw'])[elig]>=TH; truthpool.extend(truth.tolist()); ms={}
  for k,v in scores.items():
   pooled[k].extend(v[elig].tolist()); ms[k]=metrics(v[elig],truth)
  print(json.dumps(dict(seed=seed,stage='horizon',end=end,eligible=int(elig.sum()),positives=int(truth.sum()),metrics=ms)),flush=True)
 print(json.dumps(dict(stage='pooled',eligible=len(truthpool),positives=sum(truthpool),metrics={k:metrics(v,truthpool) for k,v in pooled.items()},elapsed_seconds=time.monotonic()-start)),flush=True)
if __name__=='__main__': main()
