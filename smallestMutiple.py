# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import gcd
from functools import reduce

def lcm(a,b):
    print(a, "*", b, "//", gcd(a,b), "=", a*b//gcd(a,b))
    return a*b//gcd(a,b)

x = reduce(lcm, range(1,10+1))
print(x)
y = reduce(lcm, range(1,20+1))
print(y)