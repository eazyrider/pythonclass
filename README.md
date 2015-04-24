#Jay Stahle
#Homework 1
#Python/Script Programming

name=input("Hi, What is your name?\n")
print("Hello " + name + "! Lets play a game!\n")

print("Think of a random number from 1 to 100, and I'll try to guss it!\n")

lo = 1
hi = 100
counter = 1


while lo <= hi:
	mid = (lo + hi ) // 2
	print("Is the number", mid)
	user_check = int (input ("\nEnter 1 for high, 2 for low.\n"))
	if user_check == 0:

		counter +=1


	while user_check !=1 and user_check != 2:
		user_check = int (input ( "Enter 1 for high, 2 for low.\n"))

	if user_check == 2:
		lo = mid + 1
	
	elif user_check == 1:
		hi = mid - 1
	
	else: 
		print("Thank you for playing the game\n")



