def f(s1,s2,m):
    if s1+s2<=200 or m<0:
        return m%2==0
    h=[f(s1-3,s2-4,m-1),f(s1-8,s2//2,m-1),f(s1//2,s2-10,m-1)]
    return any(h) if m%2==1 else all(h)

print([s for s in range(100,10000) if f(110,s,2) and not f(110,s,1)])
print([s for s in range(100,10000) if f(110,s,3) and not f(110,s,1)])
print([s for s in range(100,10000) if f(110,s,4) and not f(110,s,2)])
