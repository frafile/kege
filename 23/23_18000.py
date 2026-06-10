def prost(n):
    sm=0
    for i in range(1,n+1):
        if n%i==0:
            sm+=i
    return sm
def f(start,stop):
    if start>stop:
        return 0
    if start==stop:
        return 1
    return sum([f(start+1,stop), f(prost(start),stop)])
print(f(2,24))