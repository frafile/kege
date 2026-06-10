def prost(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def f(s,m):
    if prost(s) or m<0:
        return m%2==0
    h=[f(s+1,m-1),f(s+3,m-1),f(s*2,m-1)]
    return any(h) if m%2==1 else all(h)

print([s for s in range(1,101) if f(s,2) and not prost(s)])
print([s for s in range(1,101) if f(s,3) and not prost(s) and not f(s,1)])
print([s for s in range(1,101) if f(s,4) and not prost(s) and not f(s,2)])