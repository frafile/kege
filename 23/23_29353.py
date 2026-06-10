def f(start,stop):
    if start==14 or start>stop:
        return 0
    if start==stop:
        return 1
    return sum([f(start+1,stop),f(start*2,stop),f(start*3,stop)])
print(f(2,39))