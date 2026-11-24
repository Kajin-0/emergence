"""PET-003C: exact-solution threshold test; no dependencies or random seed."""
from decimal import Decimal as D, localcontext

with localcontext() as c:
    c.prec = 70
    for n in (20, 100, 1000, 10000):
        L = D(n)
        lo, hi = D(0), L
        rho = D("0.1")
        pred = L - D(2) / 3 * L.ln() + rho.ln() / 3
        # Monotone norm for t >= 0; avoid forming exp(L) or epsilon separately.
        for _ in range(220):
            t = (lo + hi) / 2
            x = (t - L).exp()
            y = t * x * x
            z = t * t * x * x * x  # magnitude; physical z is negative
            if x*x + y*y + z*z >= rho*rho:
                hi = t
            else:
                lo = t
        t = (lo + hi) / 2
        print(n, format(t, ".12f"), format(abs(t-pred), ".12f"))
