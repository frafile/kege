print('x y z w F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F=(not((not(x<=(not w)) and z))) and (not(w<=z))and (x<=(not z))
                print(x,y,z,w,int(F))