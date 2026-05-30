import sys
from functools import*
@cache
def f(n):
    if n<43:
        return g(n+4)
    else:
        return 2*f(n-2)-f(n-4)+2
@cache
def g(n):
    if n<11240:
        return g(n+3)+2
    elif n>=11240:
        return q(n)
@cache
def q(n):
    if n<21:
        return n+4
    else:
        return q(n-4)+2

for i1 in range(0,11300):
    q(i1)
for i2 in range(11300,0,-1):
    g(i2)
for i3 in range(0,2027):
    f(i3)
print(f(2026))



# print(f(2026))



































