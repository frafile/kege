def F(n):
    g=[]
    g=[int(x) for x in str(n)]
    s=sum(g)
    m=max(g)+min(g)
    l=g[0]
    r=g[-1]
    p1=s-l
    p2=m-r
    v=sorted([p1,p2])
    z = int(str(v[0])+str(v[1]))
    return z
for i in range(99999,9999,-1):
    if F(i)==222:
        print(i)

