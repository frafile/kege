def f(s, m):
    if s <=15 or m < 0:
        return m % 2 == 0
    h = [f(s - 3, m - 1), f(s - 7, m -1), f(s // 4, m - 1)]
    return any(h) if m % 2 == 1 else all(h)

print([s for s in range(16, 1000) if f(s, 2) and not f(s,1)])
# g=[s for s in range(16, 1000) if f(s, 2) and not f(s,1)]
# print(g)

print([s for s in range(16, 1000) if not f(s, 1) and f(s, 3)])
print([s for s in range(16, 1000) if not f(s, 2) and f(s, 4)])
