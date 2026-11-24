"""PET-007 exact integer validation of the four-generator Clifford example."""
from itertools import product
from fractions import Fraction

m = 4
N = 1 << m
b = [int(i in (0, N-1)) for i in range(N)]

def gamma(x, i, orientation):
    # Left multiplication by generator i, in ordered monomial basis.
    y = [0]*N
    for s, v in enumerate(x):
        sign = (-1)**((s & ((1 << i)-1)).bit_count())
        if i == m-1:
            sign *= orientation
        y[s ^ (1 << i)] = sign*v
    return y

def add(x, y): return [u+v for u,v in zip(x,y)]
def dot(x,y): return sum(u*v for u,v in zip(x,y))

def run(word, orientation):
    x = b[:]
    for i in word:
        x = add(x, gamma(x,i,orientation))
    scale = 2*3**(2*len(word))
    losses = tuple(Fraction(2*dot(x,x)-dot(x,gamma(x,i,orientation)),2*scale) for i in range(m))
    readout = Fraction(dot(b,x),2*3**len(word))
    return readout, losses

counts = []
for k in range(m+1):
    differing = 0
    for word in product(range(m),repeat=k):
        a, la = run(word,1)
        c, lc = run(word,-1)
        assert la == lc
        differing += a != c
    counts.append(differing)
    print(f'length={k}: schedules={m**k}, loss_mismatches=0, readout_mismatches={differing}')
assert counts == [0,0,0,0,24]
word = tuple(range(m))
print('ordered schedule readouts:', run(word,1)[0], run(word,-1)[0])
assert run(word,1)[0] == Fraction(2,81)
assert run(word,-1)[0] == 0
