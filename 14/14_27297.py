alf=sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def f(n,base):
    n=n[::-1]
    r=0
    for ch in range(0,len(n)):
        r+=(alf.index(n[ch]))*base**ch
    return r
for x in '0123456789ABCDEFGHI':
    if (f(f'2E{x}G8',19)+f(f'6F{x}BG',19))%18==0:
        print((f(f'2E{x}G8',19)+f(f'6F{x}BG',19))/9)