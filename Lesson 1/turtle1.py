from turtle import *

shape('turtle')
speed(-1)

mycolor = input("What color do u want ur circles to be?")


color(mycolor)

looptimes = int(input("How many times do u want to draw a circle?"))

for i in range(looptimes):
    circle(200)
    left(2)
    
    
mainloop()
