import numpy as np
import time, json, platform
N=16384; T=300; eta=.05; seed=12
rng=np.random.default_rng(seed)
X=np.array([[1.,0],[-1,0],[0,1],[0,-1]])
y=np.array([-.5,.7,.8,.6]); m=len(X)
centers=np.array([[.3,s*.8,t*.8] for s in [-1,1] for t in [-1,1]])
v0=np.repeat(centers,N//4,axis=0)+rng.uniform(-.03,.03,(N,3))
v0[-64:,0]=.6+rng.uniform(-.03,.03,64); v0[-64:,1]=rng.uniform(.005,.045,64); v0[-64:,2]=.8+rng.uniform(-.03,.03,64)
v0/=np.sqrt(N)
angles=np.linspace(0,2*np.pi,720,endpoint=False); probes=np.c_[np.cos(angles),np.sin(angles)]
L=np.c_[np.zeros(m),X]
cache=[]; visits=0; leaves=0
class Node:
    def __init__(self,idx):
        self.idx=idx; v=v0[idx]; self.S=v.T@v; lo=v.min(0); hi=v.max(0); self.c=(lo+hi)/2; self.r=(hi-lo)/2; self.children=None; cache.append(self)
    def split(self):
        if self.children is None:
            ax=np.argmax(self.r); idx=self.idx[np.argsort(v0[self.idx,ax],kind='stable')]; k=len(idx)//2
            self.children=(Node(idx[:k]),Node(idx[k:]))
        return self.children

def classify(node,P,old,Q):
    global visits,leaves
    visits+=1
    mid=Q@node.c; rad=np.abs(Q)@node.r
    if len(node.idx)==1:
        leaves+=1; mask=(Q@v0[node.idx[0]])>0
    elif np.all((mid-rad>0)|(mid+rad<=0)):
        mask=mid>0
    else:
        a,b=node.split(); aa,sa=classify(a,P,old,Q); bb,sb=classify(b,P,old,Q)
        if len(aa)==len(bb)==1 and np.array_equal(aa[0][2],bb[0][2]):
            return [(node,P,aa[0][2])],sa+sb
        return aa+bb,sa+sb
    return [(node,P,mask)],len(node.idx)*int(not np.array_equal(mask,old))

def arrays(front):
    P=np.stack([p for _,p,_ in front]); S0=np.stack([n.S for n,_,_ in front]); S=P@S0@P.transpose(0,2,1)
    masks=np.stack([s for _,_,s in front]); return P,S,masks

def predict(front,x):
    P,S,_=arrays(front); c=np.stack([n.c for n,_,_ in front]); r=np.stack([n.r for n,_,_ in front]); ns=np.array([len(n.idx) for n,_,_ in front]); l=np.c_[np.zeros(len(x)),x]
    q=np.einsum('gji,kj->gki',P,l); mid=np.einsum('gki,gi->gk',q,c); wid=np.einsum('gki,gi->gk',abs(q),r)
    linear=S[:,0,1:]@x.T; val=np.sum(np.where(mid>=0,linear,0),axis=0)
    err=np.sum(np.sqrt(np.maximum(0,ns*S[:,0,0]))[:,None]*np.maximum(wid-abs(mid),0),axis=0)
    return val,err

t0=time.perf_counter(); masks=(v0[:,1:]@X.T)>0; patterns,ids=np.unique(masks,axis=0,return_inverse=True)
front=[(Node(np.flatnonzero(ids==i)),np.eye(3),p) for i,p in enumerate(patterns)]; construction=time.perf_counter()-t0
start=time.perf_counter(); f0,e0=predict(front,probes); query_initial=time.perf_counter()-start
reduced_out=[]; switches=[]; groups=[]; visit_history=[]; storage=[]
start=time.perf_counter()
for k in range(T+1):
    before=visits; new=[]; sw=0
    for node,P,old in front:
        part,n=classify(node,P,old,L@P); new.extend(part); sw+=n
    front=new; switches.append(sw); groups.append(len(front)); visit_history.append(visits-before)
    P,S,mask=arrays(front); f=np.sum(mask*(S[:,0,1:]@X.T),axis=0); reduced_out.append(f.copy())
    # Logical numeric storage: original states + cached indices, c,r,S + active P and mask.
    storage.append(v0.size+sum(n.idx.size+n.c.size+n.r.size+n.S.size for n in cache)+len(front)*(9+m))
    if k==T: break
    g=(mask*(f-y))@X/m; M=np.repeat(np.eye(3)[None],len(front),axis=0); M[:,0,1:]=-eta*g; M[:,1:,0]=-eta*g
    PP=M@P; front=[(n,PP[i].copy(),mask[i].copy()) for i,(n,_,_) in enumerate(front)]
reduced=time.perf_counter()-start
start=time.perf_counter(); fT,eT=predict(front,probes); query_final=time.perf_counter()-start
v=v0.copy(); full_out=[]; full_switches=[]; old=masks
start=time.perf_counter()
for k in range(T+1):
    z=v[:,1:]@X.T; mask=z>0; full_switches.append(int(np.any(mask!=old,axis=1).sum())); old=mask
    act=np.maximum(z,0); f=act.T@v[:,0]; full_out.append(f.copy())
    if k==T: break
    r=(f-y)/m; da=act@r; dw=v[:,0,None]*((mask*r)@X); v[:,0]-=eta*da; v[:,1:]-=eta*dw
full=time.perf_counter()-start
start=time.perf_counter(); actual0=np.maximum(probes@v0[:,1:].T,0)@v0[:,0]; actualT=np.maximum(probes@v[:,1:].T,0)@v[:,0]; query_full=time.perf_counter()-start
training_err=float(np.max(abs(np.array(reduced_out)-np.array(full_out))))
assert training_err<1e-10 and switches==full_switches
assert np.all(abs(f0-actual0)<=e0+1e-10) and np.all(abs(fT-actualT)<=eT+1e-10)
th=.5; yes=(f0+e0<th)&(fT-eT>=th); no=(f0-e0>=th)|(fT+eT<th); truth=(actual0<th)&(actualT>=th)
assert np.all(truth[yes]) and not np.any(truth[no]) and not np.any(yes&no)
result=dict(python=platform.python_version(),numpy=np.__version__,seed=seed,N=N,T=T,m=m,initial_groups=len(patterns),final_groups=len(front),max_groups=max(groups),switch_events=sum(switches),switch_steps=sum(s>0 for s in switches),max_switches_step=max(switches),switch_counts=switches,group_counts=groups,visited_nodes=visits,singleton_tests=leaves,visit_counts=visit_history,cache_nodes=len(cache),peak_logical_numeric_entries=max(storage),full_parameters=v0.size,training_max_error=training_err,exact_final_queries=int((eT==0).sum()),final_max_error=float(abs(fT-actualT).max()),max_query_bound=float(eT.max()),true_acquisitions=int(truth.sum()),certified_acquisitions=int(yes.sum()),certified_nonacquisitions=int(no.sum()),abstentions=int((~(yes|no)).sum()),construction_seconds=construction,reduced_seconds=reduced,initial_query_seconds=query_initial,final_query_seconds=query_final,full_seconds=full,full_query_seconds=query_full)
print(json.dumps(result,indent=2))
