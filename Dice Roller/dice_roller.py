import random
x = "y"

while x == "y":
	
	# Generates a random number b/w 1 and 6 (including both 1 and 6)
	no = random.randint(1,6)
	
	if no == 1:
		print("1")

	if no == 2:
		print("2")

	if no == 3:
		print("3")

	if no == 4:
		print("4")

	if no == 5:
		print("5")

	if no == 6:
		print("5")
		
	x=input("Press Y to roll again or N to exit : ")
