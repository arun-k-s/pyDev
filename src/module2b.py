from turtle import *    
from random import randint
penup()
goto(-100,200)
for step in range(20):
    write (step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
forward(20)
ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-100, 200)
ada.pendown()

for turn in rage(100):
    ada.forward(randint(1,5))