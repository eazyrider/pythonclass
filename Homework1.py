#Jay Stahle
#Homework 1
#Python/Script Programming

name=input("Hi, What is your name?\n")
print("Hello " + name + "! Lets play a game!\n")

answer="yes"
while(answer=="yes"):

	print("Think of a random number from 1 to 100, and I'll try to guss it!\n")

	lo = 1
	hi = 100
	counter = 0


	while lo <= hi:
		mid = (lo + hi ) // 2
		print("Is the number", mid)
		counter +=1
		user_check = int (input ("\nEnter 1 for high, 2 for low. 0 for yes\n"))
		if user_check == 0:
			break

		if user_check == 2:
			lo = mid + 1
		
		elif user_check == 1:
			hi = mid - 1
		
		 
	print("I guessed it in "+str(counter)+"tries! Thank you for playing the game\n")

	answer=input("Do you want to play again? yes/no")

