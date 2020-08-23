
# for i in a:
#     print (i)

# for var_name in <collection>:
#   <statements>

# while <expression>:
#


# age = int(input("How old are you?"))

# if age <= 6: 
#     print("Baby")

# elif 6 < age <= 12:
#     print("Kid")

# elif 12 < age < 17:
#     print("Teen")
# else:
#     print("Adult")
from math import *


a = int(input("First side: "))
b = int(input("Second side: "))
c = int(input("Third side: "))

if a + b > c or a + c > b or b + c > b:
    if a == b or b == c or c == a:
        print("It's an isoceles triangle")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("It's a right angled triangle")
    else:
        print("It's a normal triangle")


area =((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))
area = sqrt(area) * (1/4)
print(area)