def sq(num):
    while num > 9:
        num = sum(int(x) for x in str(num))
    return num

def check(start, next):
    return sq(start) != int(str(next)[-1])

def f(start, stop):
    if start == stop: return 1
    if start > stop: return 0

    if check(start, start + 1) and check(start, start + 2):
        return sum([f(start + 1, stop), f(start + 2, stop)])
    if check(start, start + 1):
        return sum([f(start + 1, stop)])
    if check(start, start + 2):
        return sum([f(start + 2, stop)])
    return 0

print(f(12, 37))