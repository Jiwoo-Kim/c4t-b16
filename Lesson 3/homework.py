from turtle import * 

#1

for i in range(7):
	print(i, end=" ")

for i in range(6):
	print(i+100, end=" ")

j = 9

while j > 1:
	print(j, end=" ")
	j-=1

print("\n")

#2
for i in range(21):
	print(i, end="\n")

#3
user = int(input("Count: ")) + 1

m = 0

while m < user:
	print(m, end="\n")
	m+=1

#4
k = 5

while k <= 12:
	print(k)
	k += 1

#5
count = int(input("Count from 5: ")) 

q = 5

while q <= count:
	print(q)
	q += 1

#6
for i in range(20,9,-1):
	print(i)
#7

n = int(input("Enter your larger number: "))
m = int(input("Enter your smaller number: "))

if n > m: 
	for i in range(m,n+1):
		print(i)
else:
	print("You typed in wrong!")


#8
shape("triangle")
pencolor("blue")
fillcolor("yellow")
begin_fill()
for i in range(3):
	forward(100)
	left(120)

end_fill()

mainloop()

shape("triangle")
pencolor("blue")
begin_fill()
fillcolor("yellow")
circle(100)
end_fill()

mainloop()

#9
shape("triangle")
pencolor("green")

for i in range(6):
	circle(100)
	left(60)

mainloop()

#10

N = int(input("Count: "))

allsum = 0
b = 0

while b <= N:
	allsum = allsum + b
	b += 1 

print(allsum)

