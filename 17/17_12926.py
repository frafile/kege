f=open('17_12926.txt')
g=[int(x.replace('\n','')) for x in f]
mx=max(x+y+z+w for x,y,z,w in zip(g,g[1:],g[2:],g[3:]) if (abs(x)%10==abs(y)%10) and (abs(x)%10==abs(z)%10) and (abs(x)%10==abs(w)%10))




mxd=max(x for x in g if len(str(x))==2)
print(f'max:{mx} maxd:{mxd}')
sch=0
minsm=[]
for x,y,z,w,e in zip(g,g[1:],g[2:],g[3:],g[4:]):
    # print(f'{x},{y},{z},{w},{e}')
    if ((x<mx)+(y<mx)+(z<mx)+(w<mx)+(e<mx))==1 and (x+y+z+w+e)%mxd==0:
        minsm.append(x+y+z+w+e)
        sch+=1
print(f'count:{sch} minsum:{min(minsm)}')



#
# g1 = [(x+y+z+w, (x, y, z, w)) for x,y,z,w in zip(g,g[1:],g[2:],g[3:]) if (x%10==y%10) and (x%10==z%10) and (x%10==w%10)]
#
# g2 = [x+y+z+w for x,y,z,w in zip(g,g[1:],g[2:],g[3:]) if (x%10==y%10) and (x%10==z%10) and (x%10==w%10)]
# # for x, y, z, w in zip(g1,g2[1:], g[2:], g[3:]):
# i = 0
# for x, y, z, w in zip(g,g[1:], g[2:], g[3:]):
#     if (x%10) == (y%10) == (z%10) == (w % 10):
#         print(i)
#         print(x+y+z+w)
#         print(x, y, z, w)
#         print(x % 10, y% 10, z% 10, w% 10)
#     i += 1
