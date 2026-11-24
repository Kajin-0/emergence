"""Discrete saddle-node passage certificate; exact rational dyadic interval arithmetic."""
from fractions import Fraction as Q
from math import isqrt
from dataclasses import dataclass
import json, time, platform
BITS=96; S=1<<BITS
def down(x): return Q(x.numerator*S//x.denominator,S)
def up(x): return -down(-x)
@dataclass(frozen=True)
class I:
    lo: Q
    hi: Q
    @staticmethod
    def q(x):
        x=Q(x); return I(down(x),up(x))
    def __add__(self,o): return I(down(self.lo+o.lo),up(self.hi+o.hi))
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-o
    def __mul__(self,o):
        v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)];return I(down(min(v)),up(max(v)))
    def __truediv__(self,o):
        assert o.lo>0 or o.hi<0
        return self*I(down(1/o.hi),up(1/o.lo))
    def sqrt(self):
        assert self.lo>=0
        def floor_sqrt(x):return isqrt(x.numerator*S*S//x.denominator)
        return I(Q(floor_sqrt(self.lo),S),Q(floor_sqrt(self.hi)+1,S))
    def record(self): return {'lo':str(self.lo),'hi':str(self.hi),'approx':[float(self.lo),float(self.hi)],'width':float(self.hi-self.lo)}
def atan(x):
    assert 0<=x<=Q(1,2)
    t=x; s=Q(0)
    for k in range(64):
        s+=(-1)**k*t/(2*k+1);t*=x*x
    return I(down(s),up(s+t/129))
def atan_i(x):return I(atan(x.lo).lo,atan(x.hi).hi)
def log_q(x):
    z=(x-1)/(x+1); assert abs(z)<=Q(1,2)
    s=Q(0);t=z
    for k in range(64):s+=2*t/(2*k+1);t*=z*z
    e=2*abs(t)/(129*(1-z*z));return I(down(s-e),up(s+e))
def log_i(x):return I(log_q(x.lo).lo,log_q(x.hi).hi)
def ceil(x):return -((-x.numerator)//x.denominator)
def certify():
    delta=Q(1,10**12); root=Q(1,10**6); a=Q(1,256); b=Q(1,8); D=I.q(delta); one=I.q(1); half=I.q(Q(1,2)); four=I.q(4)
    start=time.perf_counter();x=I.q(-b);l=0
    while x.hi < -a:x=x+D+x*x;l+=1
    assert x.lo>=-a and x.hi<0
    y=I.q(b);r=0
    while y.lo>a:y=((one+four*(y-D)).sqrt()-one)*half;r+=1
    assert y.hi<=a and y.lo>0
    pi=I.q(16)*atan(Q(1,5))-I.q(4)*atan(Q(1,239))
    rooti=I.q(root)
    clock=(pi-atan_i(rooti/(-x))-atan_i(rooti/y))/rooti+half*log_i((D+y*y)/(D+x*x))
    E=8*a+8*a*a
    lower=l+r+ceil(clock.lo-E);upper=l+r+ceil(clock.hi+E)
    assert lower==upper
    elapsed=time.perf_counter()-start
    # Ordinary binary64 replay is a consistency check, not the certificate.
    z=float(-b); n=0;start=time.perf_counter()
    while z<float(b):z+=float(delta)+z*z;n+=1
    direct=time.perf_counter()-start
    assert n==lower
    print(json.dumps(dict(python=platform.python_version(),delta=str(delta),a=str(a),b=str(b),bits=BITS,forward_updates=l,inverse_updates=r,central_clock=clock.record(),clock_error_bound=str(E),exit_lower=lower,exit_upper=upper,continuous_passage_estimate=float((pi-I.q(2)*atan(Q(root,b))).lo/root),direct_exit=n,direct_endpoint=z,certificate_seconds=elapsed,direct_seconds=direct),indent=2))
if __name__=='__main__':certify()
