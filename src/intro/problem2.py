from symbulate import *

a = RV(Uniform(a=0, b=1))
b = RV(Uniform(a=0, b=1))
c = RV(Uniform(a=0, b=1))
a, b, c = AssumeIndependent(a, b, c)

x = (a+b) & (b+c)
y = RV(x, min)

sample_size = 10000
print(y.sim(sample_size).mean())
print(5.0/6)
