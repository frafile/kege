from itertools import*
g=sorted(list('АПРЕЛЬ'))
comb=list(product(g,repeat=6))
comb=[''.join(x) for x in comb]


# x=0
# for i in comb:
#     x+=1
#     if (i[0] != 'А' and i[0] != 'Л') and i.count('П') > 1 and x%2!=0:
#         print(x)
#         break
print(comb[x-1])

