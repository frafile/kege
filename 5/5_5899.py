from itertools import*
def prost(m):
    for i in range(2,m):
        if m%i==0:
            return False
    return True


def F(n):
    g=[]


    g=[int(x) for x in str(n) if x != '-']

    g_1 = (int(x) for x in str(n) if x != '-')



    v=list(permutations(g,2))
    h=[x for x in v if x[0] != 0]
    # for i in range(len(v))
    #     x = v[i]
    #     if x...
    #

    # g=[]
    # g=[int(x) for x in str(n) if x != '-']
    # v=list(permutations(g,2))
    # i=0
    # while i < len(v):
    #     if v[i][0]==0:
    #         v.pop(i)
    #         i-=1
    #     i+=1

    h=[x[0]*10+x[1] for x in h ]
    h=list(set(h))
    h=[x for x in h if prost(x)]
    fSpis = []
    for prostCh in h:
        for simvol in str(prostCh):
            if str(prostCh).count(simvol) == str(n).count(simvol):
                fSpis.append(prostCh)


    print(f"list {fSpis}")
    return len(h)



mx=0
z=-1
# for x in range(999, 99, -1):
#     print(F(x))
#     if F(x)>mx:
#         mx=F(x)
#         z=x
print(F(133))

tup = (1, 2)

print("".join(['1', '2', '3']))
print("----".join(['1', '2', '3']))


