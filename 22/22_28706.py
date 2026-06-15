f=open('22_28706')
g=[x.split() for x in f]
processes={'0':(0,0)}
while len(processes)<len(g)+1:
    for x in g:
        id=x[0]
        time=int(x[1])
        zavis_proces=[y for y in x[2].split(';')]
        if all(z in processes for z in zavis_proces):
            tmax=max([processes[v][1] for v in zavis_proces])
            processes[id] = (tmax,tmax + time)
sch=0
for start,stop in processes.values():
    if (22 > start >=9) and (22 >=  stop >= 9):
        sch+=1
print(sch)