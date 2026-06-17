from fnmatch import*
for ch in range(0,10**10+1,9874):
    if fnmatch(str(ch),'89*6?7?9?'):
        print(ch,ch/9874)