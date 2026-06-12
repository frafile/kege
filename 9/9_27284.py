f=open('9_27284.txt')
g=[str(x).replace('\t',' ').replace('\n','') for x in f]
# print(g)
g=[[int(y) for y in x.split(' ')] for x in g]
sch=0
for x in g:
    if x.count(min(x)) == 2 or x.count(min(x))==3:
        g1=[y for y in x if y != min(x)]
        if len(set(g1))==len(g1):
            if (min(g1)+max(g1))>(sum(g1)-(min(g1)+max(g1))):
                sch+=1
print(sch)