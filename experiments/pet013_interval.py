from fractions import Fraction as Q
from dataclasses import dataclass
import json
S=2**80
def floorq(x):return Q(x.numerator*S//x.denominator,S)
def ceilq(x):return -floorq(-x)
@dataclass(frozen=True)
class I:
    lo:Q
    hi:Q
    @staticmethod
    def scalar(x):
        x=Q(x);return I(floorq(x),ceilq(x))
    def __add__(self,o):
        return I(floorq(self.lo+o.lo),ceilq(self.hi+o.hi))
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-o)
    def __mul__(self,o):
        c=[a*b for a in [self.lo,self.hi] for b in [o.lo,o.hi]]
        return I(floorq(min(c)),ceilq(max(c)))
    def pow(self,n):
        out=I.scalar(1);x=self
        while n:
            if n&1:out=out*x
            n//=2
            if n:x=x*x
        return out
    def record(self):return {'lower':str(self.lo),'upper':str(self.hi),'approx':[float(self.lo),float(self.hi)],'width':float(self.hi-self.lo)}
T=10**9;k=48;s=T-k
# A/Lambda eigenvalues 1,1/3,2/3, with eigenvectors (1,1,0),(1,-1,0),(0,0,1).
p=I.scalar(Q(9,80));q=I.scalar(Q(1,80))*I.scalar(Q(1,3)).pow(s)
a=p+q;u=p-q;v=I.scalar(Q(3,40))*I.scalar(Q(2,3)).pow(s)
for r in range(k,0,-1):
    z=I.scalar(Q(1,3))*I.scalar(Q(2,3)).pow(2*r)
    # normalized linear part (2a+u)/3,(a+2u)/3,2v/3
    third=I.scalar(Q(1,3));two=I.scalar(2)
    a,u,v=third*(two*a+u)-z*a*(u*u+v*v),third*(a+two*u)-z*a*a*u,third*two*v-z*a*a*v
# general quadratic bound: C=e^2/3 < 8/3 (rho=1/4,Lambda=3/2,b=1,c=3)
err=Q(8,3)*Q(2,3)**k
assert err<Q(1,10**8)
e=I.scalar(err); pad=I(-e.hi,e.hi)
a=a+pad;u=u+pad;v=v+pad
out=a*u
assert out.lo>Q(125,10000) and out.hi<Q(126,10000)
print(json.dumps(dict(T=T,tail_steps=k,dyadic_bits=80,truncation_bound=str(err),truncation_bound_float=float(err),state=[a.record(),u.record(),v.record()],output=out.record(),certified_above_0_0125=True,certified_below_0_0126=True),indent=2))
