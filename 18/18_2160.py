import copy

f=open('18_2160')
g=[x.replace('\t',' ').replace('\n','') for x in f]
data=[]
for x in g:
    data.append(list(map(int, x.split())))
sums=set()
n=len(data)
# print(m,n)
def f(x,y,st, sum):
    if x<0 or x>n-1 or y>n-1 or y<0:
        sums.add(sum)
        print(f"sums borders: {x} {y}    {sums}       {st}")
        return
    num = data1[x][y]
    if num<st or num==0:
        sums.add(sum)
        print(f"sums number: {x} {y}    {sums}       {st}")
        return
    # data1[x][y]=0

    # return num + f(x-1,y,num) + f(x,y-1,num) + f(x+1,y,num) + f(x,y+1,num)
    sum += num
    f(x - 1, y, num, sum)
    f(x, y - 1, num, sum)
    f(x + 1, y, num, sum)
    f(x, y + 1, num, sum)



mx = 0
for x in range (n):
    for y in range(n):
        sums = set()
        data1 = copy.deepcopy(data)
        f(x, y, data1[x][y], 0)
        print(f"{x}, {y}:  {sums}")
        mx = max(mx, max(sums))
print(mx)

# data1 = copy.deepcopy(data)
# f(0, 0, data1[0][0], 0)