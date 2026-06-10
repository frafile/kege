def f(s,m):
    if s>=124 or m<0:
        return m%2==0
    h=[f(s+1,m-1), f(s+5,m-1), f(s*3,m-1)]
    return any(h) if m%2==1 else all(h)

print([s for s in range(1,124) if f(s,2)])
print([s for s in range(1,124) if f(s,3) and not f(s,1)])
print([s for s in range(1,124) if (f(s,4) or f(s,2)) and not f(s,2)])