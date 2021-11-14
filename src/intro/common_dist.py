# https://dlsun.github.io/symbulate/common_continuous.html
# https://en.wikipedia.org/wiki/Continuous_uniform_distribution
from symbulate import *
import matplotlib.pyplot as plt

dist = Uniform(a=0, b=1)  # create a new distribution
dist.plot()  # plot it
plt.show()  # show the plot, just a horizontal line, all x has equal chances.

X = RV(dist)  # create a random variable with the distribution
simu = X.sim(1000)  # simulate the variable
print(f'simu mean: {simu.mean()}')
print(f'true mean: {dist.mean()}')  # from 2nd link

print(f'simu var: {simu.var()}')
print(f'true var: {dist.var()}')  # from 2nd link
