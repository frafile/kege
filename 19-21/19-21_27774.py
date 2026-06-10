def f(s1,s2,m):
    if s1+s2>=207 or m<0:
        return m%2==0
    h=[f(s1+1,s2,m-1),f(s1*2,s2,m-1),f(s1,s2+1,m-1),f(s1,s2*2,m-1)]
    return any(h) if m%2==1 else all(h)

print([s for s in range(1,190) if f(17,s,2)])
print([s for s in range(1,190) if f(17,s,3) and not f(17,s,1)])
print([s for s in range(1,190) if f(17,s,4) and not f(17,s,2)])