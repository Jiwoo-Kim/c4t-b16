books = ["book 1", "harry potter", "book 3"]


while True:
    userInput = input("Enter here: ")
    # for book in books:
    #     if userInput == book:
    #         print(book)
    #         break
    #     else:
    #         print("Not found, try again")

    if userInput in books:
        place = books.index(userInput)
        print(books[place])
        break