print("14_19406")
symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

def to_10(s, base):
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = reversed(s)
    res = 0
    for i, x in enumerate(s):
        res += symbols.index(x) * base ** i
    return res

for x in reversed(numbers):
    res = to_10(f"6{x}QR{x}", 35) + to_10(f"{x}59SH", 35) + to_10(f"PH{x}69YW", 35)
    max_num = 0
    max_count = 0
    for n in reversed(numbers):
        m = str(res).count(n)
        if m > max_count:
            max_count = int(m)
            max_num = int(n)
    if res % max_num**2 == 0:
        print(res // max_num**2)
        break





