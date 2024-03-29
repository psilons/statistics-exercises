# solution 1 for problem1 with formulae
from sympy import *

x, c = symbols("x c")

f1 = 2 * x * x - x ** 4
r1 = integrate(f1, (x, 0, c), (c, 0, 1))
print(r1)

f2 = 2*x - 2*x*x + x*(2*c - c*c)
r2 = integrate(f2, (x, c, 1), (c, 0, 1))
print(r2)

f3 = - x**4 + 6 * x**3 - 8 * x*x + (2*x - x*x)*(3 + 2*c - c*c)
r3 = integrate(f3, (x, 1, 1+c), (c, 0, 1))
print(r3)

res = r1 + r2 + r3
print(res)

# 2/15
# 7/20
# 7/45
# 23/36
