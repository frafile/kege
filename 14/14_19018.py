alf=sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
sch=0
def f(n,base):
    n=n[::-1]
    r=0
    for ch in range(0,len(n)):
        r+=(alf.index(n[ch]))*base**ch
    return r
g16=[]
for z1 in '123456789ABCDEF':
    for z2 in '0123456789ABCDEF':
        g16.append(z1+'E'+z2)
g4=[]
for z1 in '123':
    for z2 in '0123':
        for z3 in '0123':
            for z4 in '0123':
                for z5 in '0123':
                    g4.append(z1+z2+z3+z4+z5+'2')
for ch16 in g16:
    for ch4 in g4:
        if f(ch16,16)==f(ch4,4):
            sch+=1
print(sch)