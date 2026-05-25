# from common import*
# chisla=0
# for i in range(-99999,-9999):
#     x=sistem(i,7)
#     if x.count('0') == 1 and x.count('1') <=2:
#         chisla+=1
# for t in range(10000,100000):
#     y=sistem(t,7)
#     if y.count('0') == 1 and y.count('1') <=2:
#         chisla+=1
# print(chisla)
# print(str(sistem(43526,7)))
from itertools import*
g=sorted(list('0123456'))
comb=list(product(g,repeat=5))
# print(comb)
comb=[''.join(x) for x in comb]
# print(comb)
x=0
for i in comb:
    if i.count('0')==1 and i.count('1')<=2 and i[0]!='0':
        x+=1
print(x)