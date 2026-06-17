import time


def f(n):
    dl=0
    for x in range(2,n+1,2):
        if n%x==0 and dl<5:
            dl+=1
        if dl>=5:
            break
    return dl==3

def f1(num):
    dels = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            dels.add(i)
            dels.add(num // i)

    return dels

factors = []
n = 8
# 1. Сначала полностью извлекаем базовые простые числа: 2, 3 и 5
for base in:
    while n % base == 0:
        factors.append(base)
        n //= base

s_all = time.perf_counter_ns()
for ch in range(113_000_000,114_000_000):
    # print(ch)
    d, chet = f1(ch)
    if chet == 3:
        print(ch, d)
end_all = time.perf_counter_ns()
print("all time")
print((end_all - s_all))
print("all time finish")




start = time.perf_counter()
d = f1(130_000_000)
stop = time.perf_counter()
print((stop - start) * 1000)

start = time.time_ns()
f1(130_000_000)
stop = time.time_ns()
print((stop - start) / 1_000_000)


print(d)
print(len(d))

# print(f1(130_000_000))
print(f1(113010578))