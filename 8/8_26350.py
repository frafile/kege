from itertools import*
g = sorted(list('ТАРКИ'))
print(g)
s=list(product(g,repeat=7))
s=[''.join(x) for x in s]
print(f"after join    {s}")
x=0
for i in s:
    x+=1
    if (x%2==0 and (i[0]=='Т' or i[0]=='Р' or i[0]=='К') and (i.count('ААА') or i.count('ААИ')
    or i.count('АИИ') or i.count('ИИИ') or i.count('ИИА') or i.count('ИАА') or i.count('ИАИ')
    or i.count('АИА') and (i.count('А') + i.count('И'))==3)):
        print(x)
        break
