from itertools import*
s=set(permutations('КОНФЕТЫ ИЛИ ЖИЗНЬ',7))
# print(len(s))

x=0
for i in s:
    if ''.join(i).count('  '):
        x+=1
print(x)



