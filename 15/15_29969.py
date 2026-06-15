for A in range(1,1000):
    res = True
    brk=False
    for x in range(1,1000):
        if brk==False:
            for y in range(1,1000):
                if ((x>A) or (y>A) or ((x+(2*y))<80)) == False:
                    res = False
                    brk=True
                    break
        else:
            break
    if res==True:
        print(A)