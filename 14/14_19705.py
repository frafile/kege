


for x in range(2005, 0, -1):
    f = 43**56 + 113**841 - x
    s = ''
    while f > 0:
        s = str(f % 4) + s
        f //=4
    chet = s.count('0') + s.count('2')
    nechet = s.count('1') + s.count('3')

    # верхнее решение тоже рабочее. Если оно не нужно или непонятно, выкинь его
    # if sum(1 for c in s if c in "02") % 2 == 0 and sum(1 for c in s if c in "13") % 2 == 0 and s.count('2') <= 712:
    if chet % 2 == 0 and nechet % 2 == 0 and s.count('2') <= 712:
        print(x)
        break
