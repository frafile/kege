import sys

sys.setrecursionlimit(10**10)


from functools import *

@cache
def F(n):
    if n < 10:
        return n
    # return F(n % 10) + F(n // 10)
    return n % 10 + F(n // 10)

for i in range(0, 2**63):
    F(i)