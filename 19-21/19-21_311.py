def f(s,m):
    print(s,m)
    if s<=0:
        return m%2==0
    h=[]
    for x in range(s//2,1,-1):
        h.append(f(s-x,m+1))
        print(h)
    return any(h) if m%2==1 else all(h)
print([s for s in range(5,10) if f(s,1)])