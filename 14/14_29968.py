x=0
for x in range(0,3_001):
    f = (9 * 11 ** 210) + (8 * 11 ** 150) - x
    n=f
    sch=0
    while n>0:
        if n%11==0:
            sch+=1
        n=n//11
    if sch==60:
        print(x)