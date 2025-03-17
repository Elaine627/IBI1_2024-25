# What does this piece of code do?
# Answer: Output times of trials needed to draw two random integers ranging from 1 to 6, and get two integers that are equal

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# Store times of trials in a variable called progress
progress=0 # Initialize this variable
while progress>=0: 
	progress+=1  # Record a new trial
	# Draw two random integer ranging from 1 to 6
	first_n = randint(1,6)
	second_n = randint(1,6)
	# For each trial, see if the two integers are equal
	# End the while-loop if they are equal, and print the times of trials completed as output 
	if first_n == second_n:
		print(progress)
		break

