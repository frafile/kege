A=range(6,47)
B=[x for x in range(2,161) if 161%x==0]
for y in range(4,100000):
    res =True
    C=[x for x in range(2,y) if y%x==0]
    if C:
        for x in range(1,1000000):
            if (((not(x in B)) and (x in A)) or (not (x in C)))==False:
                res=False
                break
        if res==True:
            print(y)
def mod(n):
    if n<0:
        return -n
    else:
        return n