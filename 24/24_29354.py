s= open('24_29354.txt').readline()
# s='ADHJAFHKAHSLKJHFBCLOHDASHHJDFGSBCDFSUFH'
bcs = 0
mx=-10000
st=''
for i in range(0,len(s)):
    st+=s[i]
    if st[-2:]=='BC':
        bcs+=1
    while bcs>190:
        if st[0:2]=='BC':
            bcs-=1
        st=st[1:]
    if bcs==190:
        mx=max(mx,len(st))
    if i%100_000==0:
        print(i)
print(mx)