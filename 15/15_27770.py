def fel(n,m):
    return n%m==0

for A in range(1,10000):
    res=True
    for x in range(1,1000):
        if (fel(x,21) <= ((not(fel(x,A))) <= (not(fel(x,77)))))==False:
            res=False
            break
    if res==True:
        print(A)