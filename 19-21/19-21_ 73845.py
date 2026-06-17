def f(s,m):
    # print(s,m)
    if s<=19:
        return m%2==0
    if m==0:
        return False
    h=[f(s-5,m-1)]
    if s%2==0:
        h.append(f(s//2,m-1))
    if s%3==0:
        h.append(f(s//3,m-1))
    if s%2!=0 and s%3!=0:
        h.append(f(s+1,m-1))
    return any(h) if m%2!=0 else all(h)

print([s for s in range(20,1000) if f(s,2) and not f(s,1)])
# print([s for s in range(19,1000) if f(s,3) and not f(s,1)])
# print([s for s in range(19,1000) if f(s,4) and not f(s,2)])
