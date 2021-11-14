# https://muddyhats.com/2018/11/06/estimating-expectations-and-variances-using-python/

# In a bag there are 4 blue and 5 red balls. We randomly take 3 balls from the
# bag without replacement. Let the random variable X denote the number of blue
# balls we get. Find out the expectation and variance of X.

# P(X=1) = 20/42, P(X=2) = 15/42, P(X=3) = 2/42
# E[X] = ∑xP(X=x) = 4/3
# E[X^2] = ∑x^2P(X=x) =
# Var(X) = E[(X−E(X))2] = E[X^2]−(E[X])^2 = 5/9 <-- seems wrong
from symbulate import *

P = BoxModel([0, 0, 0, 0, 0, 1, 1, 1, 1], size=3)  # 0: red, 1: blue
X = RV(P, sum)
sim = X.sim(100000)
print(sim.mean())
print(sim.var())

y = (X & X*X).sim(100000)
print(y[1].mean() - (y[0].mean()) ** 2)
