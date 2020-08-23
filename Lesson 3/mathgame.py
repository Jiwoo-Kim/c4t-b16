from random import *


while True: 
    a = randrange(10)
    b = randrange(10)
    correct = a + b

        # print(a, "+", b, "=", incorrect)
        # userInput = input("Enter true or false: ")


        # if correct != incorrect:
        #     if userInput.lower() == "t":
        #         print("You lose")
        #     elif userInput.lower() == "f":
        #         print("You win!")
        # if correct == incorrect:
        #     if userInput.lower() == "f":
        #         print("You lose")
        #     elif userInput.lower() == "t":
        #         print("You win!")
            


    wrongNumber = [-1, 0, 1]

    incorrect = correct + choice(wrongNumber)

    print(a, "+", b, "=", incorrect)
    userInput = input("True or False (T/F): ")

    if incorrect != correct:
        if userInput.lower() == "t":
            print("You lose")
        elif userInput.lower() == "f":
            print("You win!")
    else:
        if userInput.lower() == "t":
            print("You win!")
        elif userInput.lower() == "f":
            print("You lose")