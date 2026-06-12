from itertools import*
g = product('ВЬЮГА',repeat=6)
g = [''.join(x) for x in g]
sch=0
for i in g:
    if i.count('ЮГ'):
        print(i)
        sch+=1
print(sch)