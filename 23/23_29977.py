def f(start,stop):
    print(start)
    if start==9 or start<stop:
        return 0
    if start==stop:
        return 1
    return sum([f(start-1,stop),f(start-3,stop),f(start//2,stop)])

print(f(19,12)*f(12,3))