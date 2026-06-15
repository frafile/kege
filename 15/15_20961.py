P=range(15,143)
Q=range(38,168)
mn=100000
for i in range(15,168):
    for j in range(168, i-1,-1):
        A=range(i,j+1)
        res=False
        for x in range(1,1000):
            if (not((x in Q) <= (((not (x in A)) and (x in P)) <= (not (x in Q)))))==True:
                res=True
                break
        if res==False:
            mn=min(mn,j-i)
            # print(mn,j,i,len(A), A)
# print(mn)
print(2|6)