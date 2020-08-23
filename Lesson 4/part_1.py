#1
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print("Hi,", first_name, last_name)

#2
word = input("Capitalize this word: ")
print(word.upper())

#3
num = int(input("Square this number: "))
print(num**2)

#4
from turtle import *

radius = int(input("What do you want the radius to be: "))
circle(radius)
mainloop()