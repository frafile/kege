f=open('9_28755.txt')
g=[str(x).replace('\t',' ').replace('\n','') for x in f]
g=[[int(x) for x in y.split(' ')] for y in g]
# print(g)
sch=0
for i in g:
    if max(i)<(sum(i)-max(i)):
        if i[0]+i[1]!=i[2]+i[3] and i[0]+i[2]!=i[1]+i[3] and i[0]+i[3]!=i[1]+i[2]:
            sch+=1
print(sch)