f=open('17_23952.txt')
g=[int(x.replace('\n','')) for x in f]
mx=max([x for x in g if x%100==93])
s=0
sm=0
print(f'Max:{mx}')
# print(list(zip(g,g[1:])))
for x,y in zip(g,g[1:]):
    if ((x>mx) + (y>mx))==1  and (str(x)[0]=='9' or str(y)[0]=='9'):
        # print(x,y)
        if x>mx:
            sm+=x
        if y>mx:
            sm+=y
        s+=1
print(f'Count:{s} Sum:{sm}')