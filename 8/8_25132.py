from itertools import*
sim=sorted('СДАЙЕГЭ')
g=list(product(sim,repeat=6))
g=[''.join(x) for x in g]
sm=0
for ind,x in enumerate(g):
    num=ind+1
    if x.count('ЕГЭ')>0:
        sm+=num
        # print(x)
print(sm)