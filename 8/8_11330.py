from itertools import*
sim=('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
# g = product(sim,repeat=11)
g = product(sim,repeat=11)

etalon = tuple('ИНФОРМАТИКА')

def f(n,base,symbols):
    sm=0
    n=n[::-1]
    for i,x in enumerate(n):
        sm+=symbols.index(x)*base**i
    return sm
# print(f("ЮЯ",33))
print(f('ЯЯЯЯЯЯЯЯЯЯЯ',33,'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')-f('ИНФОРМАТИКА',33,'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')+1)