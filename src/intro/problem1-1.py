# solution for problem1 with formulae
from sympy import *

x, c = symbols("x c")

f1 = (1 - x*x/2) ** 2
r1 = integrate(f1, (x, 0, c), (c, 0, 1))
print(r1)

f2 = (1 - x + c - c*c/2) ** 2
r2 = integrate(f2, (x, c, 1), (c, 0, 1))
print(r2)

f3 = (Rational(3, 2) - 2*x + x*x/2 + c - c*c/2) ** 2  # need rational to keep final result rational
r3 = integrate(f3, (x, 1, 1+c), (c, 0, 1))
print(r3)

res = r1 + r2 + r3
print(res)

# 17/40
# 23/120
# 1/45
# 23/36
