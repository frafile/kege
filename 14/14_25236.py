def f(n,sist):
    r=0
    symbols = "0123456789ABC"
    print(symbols.index("B"))
    return
    for i in range(len(n) - 1, -1 , -1):
        if n[i]=='A':
            chis = 10
        else:
            chis=int(n[i])
        r+= chis * sist ** (len(n) - i - 1)
    return r
for p in range(36, 10, -1):
    for x in range(1,500_001):
        ch1="29A1"
        ch2="47771"
        ch3='12A'
        if (f(ch1,p)+f(ch2,p)+f(ch3,p)) ==  1_000_000 + x:
            print(p)

# print(f("29A1", 11))