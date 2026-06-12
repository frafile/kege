from itertools import*
f=open("9_14249.txt")
g=[str(x).replace('\n','') for x in f]
g=[[int(y) for y in x.split('\t')] for x in g]
for ind,x in enumerate(g):
    chet=len([y for y in x if y%2==0])
    nechet=len([y for y in x if y%2!=0])
    if chet==nechet:
        h=permutations(x)
        h=set(h)
        for z in h:
            if (z[0]+z[1])==(z[2]+z[3])==(z[4]+z[5]):
                print(ind+1)