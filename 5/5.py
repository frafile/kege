def three(t,y):
    s=[]
    while t>0:
        s.append(str(t%y))
        t //= y
    return ''.join(reversed(s))

def F(n):
    x=three(n,3)
    if n%3==0:
        x = "1"+x+"02"
    else:
        x = x + three((n%3)*5,3)
    return(x)

for i in range(1,1000):
    r=int(F(i),3)
    if r>=177:
        print(i)




