print('c a d b')
for c in 0,1:
    for a in 0, 1:
        for d in 0, 1:
            for b in 0, 1:
                if (((a and b) == (not c)) and (b <= d))==1:
                    print(c,a,d,b)