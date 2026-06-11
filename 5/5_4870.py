from itertools import*
def f(n):
    g = set(permutations(str(n),2))
    g = [int(''.join(x)) for x in g if x[0]!='0']
    return max(g) - min(g)
sch=0
for i in range(300,401):
    if f(i)==20:
        sch+=1
print(sch)

print(sum(1 for x in range(300, 401) if f(x) == 20))