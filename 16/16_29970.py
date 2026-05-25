import sys

sys.setrecursionlimit(10**6)



def F(n):
    return 3 * G(n - 3) + 7

def G(n):
    if n > 20:
        return G(n - 3) + 1
    else:
        return n + 2

print(F(37811))

print(548 - 527 // 8 * 8)
# print(F(37811))