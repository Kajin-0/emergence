import math
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction as Q

def exact(n,x):
    z=[Q(i+1,n+1) for i in range(n+1)]
    w=[Q((-1)**(n-i)*math.comb(n,i),2**n) for i in range(n+1)]
    v=sum(wi/(1-x*zi) for wi,zi in zip(w,z))
    closed=math.factorial(n)*(x/Q(n+1))**n/(2**n*math.prod(1-x*zi for zi in z))
    assert v==closed
    return v
for n in [2,4,6,8,12,16]:
    a=exact(n,Q(1,5)); b=exact(n,Q(9,10)); c=exact(n,1-Q(1,2**n))
    print(f'n={n:2d} early={float(a):.12g} future={float(b):.12g} amplification={float(b/a):.12g} nearpole={float(c):.12g}')
# Finite grid: known capacities, exact minimax formula. Numeric LP checks only.
n=8; z=np.arange(1,n+2)/(n+1); cap=np.array([math.comb(n,i)/2**n for i in range(n+1)])
for m in [1,3,5,9]:
    x=np.linspace(0,.2,m) if m>1 else np.array([.2]); A=1/(1-x[:,None]*z); h=1/(1-.9*z); delta=1e-5
    p=linprog(-h,A_ub=np.r_[A,-A],b_ub=np.full(2*m,delta),bounds=list(zip(-cap,cap)),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    # variables alpha+,alpha-, residual t>=0, abs residual<=t
    B=np.c_[A.T,-A.T,np.eye(n+1)]
    # h - A.T alpha <= t, A.T alpha - h <=t
    M=np.r_[np.c_[-A.T,A.T,-np.eye(n+1)],np.c_[A.T,-A.T,-np.eye(n+1)]]
    d=linprog(np.r_[np.full(2*m,delta),cap],A_ub=M,b_ub=np.r_[-h,h],bounds=(0,None),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    assert p.success and d.success
    alpha=d.x[:m]-d.x[m:2*m]
    ub=cap@abs(h-A.T@alpha)+delta*sum(abs(alpha))
    # rescale primal to feasibility, avoiding treating LP tolerance as proof
    w=p.x; w=w*min(1,delta/max(delta,np.max(abs(A@w))),1/max(1,np.max(abs(w)/cap)))
    lb=h@w
    print(f'm={m} lower={lb:.12g} upper={ub:.12g} gap={ub-lb:.3g} noise_gain={sum(abs(alpha)):.6g}')
