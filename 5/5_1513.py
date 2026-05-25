def F(n):
    x=bin(n)[2:]
    x=x+x[-1]
    if x.count('1')%2==0:
        x=x+'0'
    else:
        x=x+'1'
    if x.count('1') % 2 == 0:
        x = x + '0'
    else:
        x = x + '1'

    return int(x,2)
for i in range(1,10000):
    if F(i)>90:
        print(i)
        break
