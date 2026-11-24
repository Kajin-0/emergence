import numpy as np
import time, platform, json
# Fixed test: 4 distinct train patterns, both layers trained. No tuning/sweeps.
N=8192; steps=300; eta=.05; seed=11; d=2
rng=np.random.default_rng(seed)
X=np.array([[1.,0],[-1,0],[0,1],[0,-1]])
y=np.array([1.,.7,.8,.6])
centers=np.array([[.3,s*.8,t*.8] for s in [-1,1] for t in [-1,1]])
v0=(np.repeat(centers,N//4,axis=0)+rng.uniform(-.03,.03,(N,3)))/np.sqrt(N)
angles=np.linspace(0,2*np.pi,720,endpoint=False); probes=np.c_[np.cos(angles),np.sin(angles)]
def fullout(v,x): return np.maximum(x@v[:,1:].T,0)@v[:,0]
# Start both methods from identical input state; group construction counted.
t0=time.perf_counter(); masks=(v0[:,1:]@X.T)>0
patterns,ids=np.unique(masks,axis=0,return_inverse=True)
S=[]; c=[]; rad=[]; ns=[]
for i in range(len(patterns)):
 v=v0[ids==i]; m=v.mean(axis=0); S.append(v.T@v); c.append(m); rad.append(np.linalg.norm(v-m,axis=1).max()); ns.append(len(v))
S=np.array(S); c=np.array(c); rad=np.array(rad); ns=np.array(ns); P=np.repeat(np.eye(3)[None],len(S),axis=0)
construction=time.perf_counter()-t0
ell=np.c_[np.zeros(len(X)),X]
def predict(S,P,x):
 l=np.c_[np.zeros(len(x)),x]; q=np.einsum('gji,kj->gki',P,l); mid=np.einsum('gki,gi->gk',q,c); wid=rad[:,None]*np.linalg.norm(q,axis=2)
 linear=S[:,0,1:]@x.T; val=np.sum(np.where(mid>=0,linear,0),axis=0)
 error=np.sum(np.sqrt(ns*S[:,0,0])[:,None]*np.maximum(wid-np.abs(mid),0),axis=0)
 return val,error,mid,wid

t0=time.perf_counter(); minimum=1e9; starts=predict(S,P,probes)
for k in range(steps+1):
 f,err,mid,wid=predict(S,P,X); margin=np.where(patterns,mid,-mid)-wid; minimum=min(minimum,margin.min()*np.sqrt(N)); assert margin.min()>0
 if k==steps: break
 g=(patterns*(f-y))@X/len(X)
 M=np.repeat(np.eye(3)[None],len(S),axis=0); M[:,0,1:]=-eta*g; M[:,1:,0]=-eta*g
 S=M@S@M.transpose(0,2,1); P=M@P
reduced=time.perf_counter()-t0
# Includes all 720 predictions at initial and final; baseline same tasks separately timed.
t0=time.perf_counter(); final=predict(S,P,probes); query_reduced=time.perf_counter()-t0
v=v0.copy(); t0=time.perf_counter()
for k in range(steps):
 z=v[:,1:]@X.T; r=(np.maximum(z,0).T@v[:,0]-y)/len(X)
 dv_a=np.maximum(z,0)@r; dv_w=v[:,0,None]*((z>0)*r)@X
 v[:,0]-=eta*dv_a; v[:,1:]-=eta*dv_w
full=time.perf_counter()-t0
t0=time.perf_counter(); actual=fullout(v,probes); actual0=fullout(v0,probes); query_full=time.perf_counter()-t0
val,e,_,_=final; err=np.abs(actual-val); cert=e==0; assert np.all(err<=e+1e-11)
initval,inite,*_=starts; assert np.all(np.abs(actual0-initval)<=inite+1e-11)
# Fixed output target 0.5 on all probes. Acquisition means initially below, finally >=.
th=.5; yes=(initval+inite<th)&(val-e>=th); no=(initval-inite>=th)|(val+e<th); truth=(actual0<th)&(actual>=th)
assert np.all(truth[yes]) and not np.any(truth[no]); print(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,N=N,steps=steps,seed=seed,patterns=len(S),construction_seconds=construction,reduced_seconds=reduced,full_seconds=full,query_reduced_seconds=query_reduced,query_full_seconds=query_full,training_scaled_min_margin=float(minimum),training_final_max_error=float(np.max(np.abs(fullout(v,X)-f))),exact_queries=int(cert.sum()),exact_query_max_error=float(err[cert].max()),all_query_max_error=float(err.max()),largest_bound=float(e.max()),true_acquisitions=int(truth.sum()),certified_acquisitions=int(yes.sum()),certified_nonacquisitions=int(no.sum()),abstentions=int((~(yes|no)).sum()),full_params=int(v0.size),summary_scalars=int(S.size+P.size+c.size+rad.size+ns.size+patterns.size)),indent=2))
