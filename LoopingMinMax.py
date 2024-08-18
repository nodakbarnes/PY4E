#!/usr/bin/env python3

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an 
# appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below:
# Invalid input
# Maximum is 10
# Minimum is 2

largest = None
smallest = None

while True:
	num = input("Enter a number: ")
	if num == "done":
		break
	try:
		inum = int(num)
		# test for smallest
		if smallest is None or smallest > inum:
			smallest = inum
		# test for largest
		if largest is None or largest < inum:
			largest = inum
	except:
		print('Invalid input')
		
print("Maximum is", largest)
print("Minimum is", smallest)

# Enter a number: 7
# Enter a number: 2
# Enter a number: bob
# Invalid input
# Enter a number: 10
# Enter a number: 4
# Enter a number: done
# Maximum is 10
# Minimum is 2
