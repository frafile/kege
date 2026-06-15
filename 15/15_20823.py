for A in range(1,1000):
    res=True
    for x in range(1,1000):
        if ((x&A==0) <= ((x&77 == 0) and (x&44==0))) == False:
            res=False
            break
    if res==True:
        print(A)
        break