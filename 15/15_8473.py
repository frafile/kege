def fel(n,m):
    return n%m==0
P=range(5,138)
for A in range(1,1000):
    res1=False
    res2=True
    for x in range(1,1000):
        if ((fel(x,115) and (not fel(x,5))) or ((fel(A,x) <= (not fel(A,5))) and (not (A in P))))==True:
            res1=True
        else:
            res2=False
    if res1==True and res2==False:
        print(A)
        break
