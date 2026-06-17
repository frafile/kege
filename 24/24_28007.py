s=open('24_28007.txt').readline().strip()
s='(((56+-+00(0678-89)(7182-15)(3222+745))'
st=''
A = ''
B = ''
mxlen=-100000
ln=0
for i in range(0,len(s)):
    st+=s[i]
    ln+=1
    # print(st,i)
    if st[-1]=='(':
        for a in range(i+1,len(s)):
            # print(f'a:{s[a]}')
            if s[a] in '+-()':
                break
            A+=s[a]
    if A!='' and (st[-2:]=='+-' or st[-2:]=='++' or st[-2:]=='-+' or st[-2:]=='--'):
        A=''
        ln=0
        continue
    if len(st)>2 and st[-2] in '+-' and st[-1] in '0123456789' and A!='':
        for b in range(i+1,len(s)):
            # print(f'b:{s[b]}')
            if s[b] in '+-()':
                break
            B+=s[b]
    if st[-1]==')':
        if A=='' or B=='':
            ln=0
        elif (int(A)%5!=0 and int(B)%5==0)==False or (A[0]=='0' or B[0]=='0')==True:
            ln=0
        else:
            mxlen=max(mxlen,ln)
            # print(A,B)
        A=''
        B=''
        continue
    # print(f'A:{A},B:{B},Len:{ln}')
print(mxlen)