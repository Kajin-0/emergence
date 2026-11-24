"""PET-009 exact moment checks and direct gradient-flow verification.
Dependencies numpy, scipy, sympy; no randomness."""
from fractions import Fraction as Q
from math import comb
import numpy as np
from scipy.integrate import solve_ivp, quad
import sympy as sp

for q in range(5):
    n=q+4
    a=[Q(i+1,2*(n+1)) for i in range(n+1)]
    d=[(-1)**(n-i)*comb(n,i) for i in range(n+1)]
    assert all(sum(di*ai**j for di,ai in zip(d,a))==0 for j in range(n))
    s=Q(1,2)
    relation=4*sum(di*(ai/(1-2*ai*s))**2 for di,ai in zip(d,a))
    assert relation>0
    print(q,n,2**n,str(relation),float(relation))

a=np.repeat(np.arange(1,6)/10,[comb(4,i) for i in range(5)])
c=np.repeat([(-1)**(4-i)/np.sqrt(2) for i in range(5)],[comb(4,i) for i in range(5)])
b=np.sqrt(2)*a
def train(s): return 2*np.sum((a/(1-2*a*s))**3)
T,quaderr=quad(lambda s:1/(6-train(s)),0,.5,epsabs=1e-12,epsrel=1e-12)
print("F0",train(0),"F(s*)",train(.5),"quadrature estimate",quaderr)
def ode(t,z):
    aa,bb=z.reshape(2,-1)
    r=6-np.dot(aa,bb*bb)
    return np.r_[r*bb*bb,2*r*aa*bb]
sol=solve_ivp(ode,[0,T],np.r_[a,b],rtol=1e-12,atol=1e-14)
assert sol.success
aa,bb=sol.y[:,-1].reshape(2,-1)
rel=4*np.dot(aa*bb,c)
err=abs(rel-float(Q(1375,3969)))
print("T",T,"F",np.dot(aa,bb*bb),"relation",rel,"abs err",err)
print("steps",len(sol.t)-1,"nfev",sol.nfev)
assert err<1e-8
nodes=[sp.Rational(i+1,10) for i in range(5)]
mom=[sum(comb(4,i)*x**(k+3) for i,x in enumerate(nodes)) for k in range(10)]
H=sp.Matrix(5,5,lambda i,j:mom[i+j])
coef=H.inv()*sp.Matrix([-mom[i+5] for i in range(5)])
z=sp.symbols("z")
poly=z**5+sum(coef[i]*z**i for i in range(5))
assert sp.expand(poly-sp.prod(z-x for x in nodes))==0
print(sp.factor(poly))
