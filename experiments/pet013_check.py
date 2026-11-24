import math, json, platform, time
import numpy as np
eta=.5; lam=1+eta; rho=.25; b=1.; c=3.; xi=np.array([.125,.10,.075]); tol=1e-8
A=np.array([[1.,eta,0.],[eta,1.,0.],[0.,0.,1.]])
B=A/lam
C=4*b*rho*rho/(lam*(lam-1))*math.exp(2*c*rho/(lam*(lam-1)))
k=math.ceil(math.log(C/tol)/math.log(lam))
# a,u,v coordinates; y=(3/5,4/5) in original input basis.
def normalized_step(z,remaining):
    a,u,v=z; scale=lam**(-2*remaining)/lam
    return B@z+scale*np.array([-eta*a*(u*u+v*v),-eta*a*a*u,-eta*a*a*v])
def direct(T):
    z=xi.copy()
    for r in range(T,0,-1): z=normalized_step(z,r)
    return z
def jump(T):
    kk=min(k,T); z=np.linalg.matrix_power(B,T-kk)@xi
    for r in range(kk,0,-1): z=normalized_step(z,r)
    return z
# Untrained input x=(3/5,4/5) -> f=a*u.
rows=[]
for T in (64,1024,10000,1000000000):
    start=time.perf_counter(); p=jump(T); jump_seconds=time.perf_counter()-start
    linear=np.linalg.matrix_power(B,T)@xi
    actual=None; err=None; direct_seconds=None
    if T<=10000:
        start=time.perf_counter(); actual=direct(T); direct_seconds=time.perf_counter()-start
        err=float(np.max(np.abs(p-actual))); assert err<=tol+1e-12
    f=float(p[0]*p[1]); fl=float(linear[0]*linear[1]); ferr=4*rho*tol+tol*tol
    # fixed threshold chosen before execution; compare true nonlinear to linear prediction
    threshold=.0126
    rows.append(dict(T=T,tail_steps=min(k,T),forecast=p.tolist(),direct=actual.tolist() if actual is not None else None,state_max_error=err,output=f,linear_output=fl,output_error_bound=ferr,threshold=threshold,certified_below=f+ferr<threshold,linear_predicts_above=fl>=threshold,jump_seconds=jump_seconds,direct_seconds=direct_seconds))
print(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,rho=rho,Lambda=lam,b=b,c=c,xi=xi.tolist(),constant=C,tolerance=tol,tail_steps=k,rows=rows),indent=2))
