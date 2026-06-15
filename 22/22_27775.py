f=open('22_27775')
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
del(processes['0'])
mxt=max(x[1] for x in processes.values())
# print(mxt)
for tm in range(0,mxt):
    # print(tm)
    active_proc=[x[0] for x in processes.values() if x[0]<=tm and x[1]>tm]
    if len(active_proc)==5:
        print(active_proc,tm)



processes = dict(sorted(processes.items()))
for p in processes.values():
    times = []
    for tm in range(0,mxt):
        if p[0] <= tm and p[1] > tm:
            times.append('1')
        else:
            times.append('0')
    print(' '.join(times))
