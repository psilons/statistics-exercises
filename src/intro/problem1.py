# Problem: Given 5 random variables a, b, c, d, e over uniform distribution U(0, 1),
# find the expected value of min(a+b, b+c, c+d, d+e)

from symbulate import *  # install this lib

a = RV(Uniform(a=0, b=1))  # define random variables
b = RV(Uniform(a=0, b=1))
c = RV(Uniform(a=0, b=1))
d = RV(Uniform(a=0, b=1))
e = RV(Uniform(a=0, b=1))

a, b, c, d, e = AssumeIndependent(a, b, c, d, e)

x = (a+b) & (b+c) & (c+d) & (d+e)  # create 4 columns for sums
y = RV(x, min)  # find min in each row

sample_size = 10 ** 6
print(y.sim(sample_size).mean())  # 0.6388566234499824 0.638871919002973
