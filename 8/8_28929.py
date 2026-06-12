from itertools import*
sim=sorted('СИМВОЛ')
g = list(product(sim, repeat=5))
# print(list(g))
# help(itertools.product)
for ind,x in enumerate(g):
    n=ind+1
    if n%2!=0 and x[0]!='О' and x[0]!='С' and x.count('В')==1 and x.count('С')<=1:
        print(n,x)