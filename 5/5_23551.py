def f(n):
    x=bin(n)[2:]
    if n%2==0:
        x='10'+x
    else:
        x = '1' + x +  '01'
    return int(x,2)
for i in range(1000,1,-1):
    if f(i)<30:
        print(i)
        break