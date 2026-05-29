


for x in range(1000, 10000):
    s= []
    x = str(x)
    g = sorted([int(x[0]) * int(x[1]), int(x[0]) * int(x[2]), int(x[0]) * int(x[3])])
    if str(g[-2]) + str(g[-1]) == '5472':
        print(x)
        break