f=open('22_29352')
g=[x.split() for x in f]
processes= {'0': 0}
print(processes['1'])
while len(processes)<(len(g)+1):
    for x in g:
        id=x[0]
        if id in processes:
            continue
        time=int(x[1])
        zavis_proc=[y for y in x[2].split(';')]
        if all(proc in processes for proc in zavis_proc):
            tmax=max(processes[zp] for zp in zavis_proc)
            processes[id] = tmax + time

print(max(processes.values()))