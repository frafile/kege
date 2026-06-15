from turtle import*
pendown()
left(90)
k=10
tracer(0, 0)
for i in range(3):
    forward(32*k)
    right(90)
    forward(38*k)
    right(90)
penup()
forward(25*k)
right(90)
forward(21*k)
left(90)
pendown()
for i in range(3):
    forward(29*k)
    right(90)
    back(18*k)
    right(90)
penup()
for x in range(-10,100):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(2, 'red')
done()

print(33*39 + 30 * 19 - 19 * 8 )