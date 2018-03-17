from turtle import *
# speed()
penup()
goto(-100,140)
for step in range(100):
    write (step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)