def f(s1,s2,m):
    if s1+s2>=154 or m<0:
        return m%2==0
    h=[f(s1+4,s2,m-1),f(s1*3,s2,m-1),f(s1,s2+4,m-1),f(s1,s2*3,m-1)]
    return any(h) if m%2==1 else all(h)

print([s for s in range(1,143) if f(11,s,2)])
print([s for s in range(1,143) if f(11,s,3) and not f(11,s,1)])
print([s for s in range(1,143) if f(11,s,4) and not f(11,s,2)])

()


