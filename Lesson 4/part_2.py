#1
for i in range(3,13):
    print(i,end=" ")

n = int(input("Please enter a number: "))

#2
for i in range(0, n+1):
    print(i, end=" ")

#3
m = int(input("Count to and from this number: "))

if m % 2 == 0:
    m -= 1

for i in range(m, 0, -2):
    print(i, end=" ")

print("\n")

for i in range(1, m+1, 2):
    print(i, end=" ")

#4
from turtle import *

sides = int(input("Number of sides of the polygon: "))

angle = (360/sides)

for i in range(sides):
    forward(100)
    left(angle)

mainloop()

