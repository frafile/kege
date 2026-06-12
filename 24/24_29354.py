s = open("24_29765.txt").readline()

temp = ''
k = 0
m = 0

for i in range(len(s)):
    temp += s[i]
    if temp[-2:] == 'BC':
        k += 1
    while k > 180:
        if temp[:2] == 'BC': k -= 1
        temp = temp[1:]
    if k == 190:
        m = max(len(temp), m)
    if i % 100_000 == 0:
        print(i, m)

print(m)
