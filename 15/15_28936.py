def f(x,y):
    return x*y<A or 5*x<y or 486<=x
for A in range(0,2_000_000):
    if all(f(x,y) for x in range(0,487) for y in range(0,2430)):
        print(A)
        break