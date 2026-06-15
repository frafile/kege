P = range(25,65)
Q = range(40,116)
minl=10000
gt = tuple()
for i in range(25,116):
    for j in range(115,24,-1):
        if j<=i:
            continue
        A=range(i,j+1)
        # print(A)
        g=[]
        res=True
        for x in range(1,10000):
            if ((x in P)<=(((x in Q) and (not (x in A))) <= (not(x in P))))==False:
                res=False
                break
            # g.append(((x in P)<=(((x in Q) and (not (x in A))) <= (not(x in P)))))
        if res==True:
            # print(len(A))
            minl = min(minl, j - i)
            # if (i == 40 and j == 65):
            #     print(len(A))
            gt = (P, Q, A, i, j)

print(minl)
print(gt)
# print(((x in P)<=(((x in Q) and (not (x in range(40,65)))) <= (not(x in P)))))