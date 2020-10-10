stock = {
    "hp": 20,
    "dell": 50,
    "macbook": 12,
    "asus": 30,
}

stock["toshiba"] = 10

# print(stock['macbook'])

# computer = input("Check stock: ").lower()

# print(stock[computer])

# newKey = input("Input the new type of computer: ").lower()

# newValue = int(input("Input how many of those computers you have: "))

# stock[newKey] = newValue

stock['dell'] += 10
stock['macbook'] = 2

for i in stock:
    print (i,"-->", stock[i],end=":\n")

totalnum = 0 

for i in stock:
    totalnum += stock[i]

print(totalnum)

stock['fujitsu'] = 15
stock['alienware'] = 5

print("\n\n")

for i in stock:
    print (i,"-->", stock[i],end=":\n")

totalnum = 0
for i in stock:
    totalnum += stock[i]

print(totalnum)

###
###
###

price = {
    "hp": 600,
    "dell": 650,
    "macbook": 12000,
    "asus": 400,
    "acer": 350,
    "toshiba": 600,
    "fujitsu": 900,
    "alienware": 1000
}

print(price['asus'])

brandprice = input("Check price: ").lower()


print(brandprice, "->", price[brandprice])

print("The price of 5 ASUS is", 5*price['asus'])

keyCheckprice = input("Check price: ").lowefr()
valueCheckprice = int(input("Order amount: "))

print(valueCheckprice,keyCheckprice.upper(), "is", valueCheckprice*price[keyCheckprice])









