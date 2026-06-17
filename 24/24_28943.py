s=open('24_28943.txt').readline()
# s='A 20 B 20A'
st=''
dv=0
gl=0
num = 26
mn=10000000
for i in range(0,len(s)):
    st+=s[i]
    # print(st)
    if st[-2:]=='20':
        dv+=1
    if st[-1] in "AEIOUY":
        gl+=1
    while dv>num and gl>1:
        if st[0:2]=='20':
            dv-=1
        if st[0] in "AEIOUY":
            gl-=1
        st=st[1:]
    if dv==num and st[-1] in "AEIOUY":
        mn=min(mn,len(st))
    if i%10_000==0:
        print(i,mn)
print(mn)