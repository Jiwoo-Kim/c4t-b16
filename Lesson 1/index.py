#
# name = input("Enter your name: ")
# age = int(input("How old are you? "))
# print("Hello " + name + "!")
# print("You are " + age + "years old")

#String

#integer
1, 2, 3, 4, 192393

#float
1.1, 2.341, 3.14, 123123.123123

#List

#array = ["Jiwoo", 13]

#print(array)

# in lists, the index starts from 0 


# Dictionary

# #library = {
#     "dried things" : "snacks",
#     "drinks" : ["coke", "pepsi", "mountain dew"]
# }

# library1 = {
#     # "key" : "value",
#     "name" : "",
#     "age" : 12,
#     "class" : "IG",
#     "fav" : []
# }

# print(library1["class"]) # Get value from Key (class) of the Dictionary (library1)

# library1["age"] = 17

# print(library1["age"])

classSummaries = [
    {
        "name" :"",
        "grade" : 8.0,
        "age" : 16,
        "class" : "C4T-B16",
        "fav" : ["LOL", "CSGO"]
    },
     {
        "name" :"",
        "grade" : 9.0,
        "age" : 16,
        "class" : "C4T-B16",
        "fav" : ["Music", "Music"]
    },
     {
        "name" :"",
        "grade" : 9.5,
        "age" : 16,
        "class" : "C4T-B16",
        "fav" : ["Basketball", "Reading", "Poker"]
    }
]

print(len(classSummaries))

print("Please type in the values for the new student")

name = input("What is your name? ")
grade = float(input("What is the grade of the student? "))
age = int(input("What is the age of the student? "))
classroom = input("What class is the student in? ")

fav = []
n = int(input("How many things do you like to do? "))

for i in range(0,n):
    element = input("What do you like to do? ")
    fav.append(element)

newStudent = {
        "name" : name,
        "grade" : grade,
        "age" : age,
        "class" : classroom,
        "fav" : fav
}




classSummaries.append(newStudent)


print(newStudent)