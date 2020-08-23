#1
n = int(input("Is this greater or smaller than 13: "))

if n > 13:
    print("Greater!")
elif n < 13:
    print("Smaller!")
elif n == 13:
    print("This is 13!")

#2
m = int(input("Even or odd: "))

if m % 2 == 0:
    print("Even!")
elif m % 2 == 1:
    print("Odd!")

#3
month = input("How many days are in this month: ").lower()

thirty_one = ["january", "march", "may", "july", "august", "october", "december"]
thirty = ["april", "june", "september", "november"]

if month in thirty_one:
    print("31 Days!")
elif month in thirty:
    print("30 DAYS!")
elif month == "february":
    print("28 DAYS! (29 in leap years)")
else: 
    print("You didn't enter a month of the year")

