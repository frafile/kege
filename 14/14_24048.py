

def to_10(s, base):
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = reversed(s)
    res = 0
    for index, value in enumerate(s):
        res += symbols.index(value) * base ** index
    return res

for p in range(33, 100):
    if to_10("KOT", p) + to_10("GOLODNI", p) == to_10("MEEOW", p) * to_10("100", p) - 20194023088:
        print(p)
        print(to_10("PURR", p))
        break