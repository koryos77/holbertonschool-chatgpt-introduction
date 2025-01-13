#!/usr/bin/python3
import sys

# Function to compute the factorial of a number recursively
def factorial(n):
	"""
	Function Description:
	This function calculates the factorial of a non-negative integer `n` using recursion.
	The factorial of a number is the product of all positive integers less than or equal to that number.
	
	Parameters:
	n (int): The number for which the factorial is to be computed. It must be a non-negative integer.
	
	Returns:
	int: The factorial of the number `n`. If `n` is 0, the function returns 1 as 0! = 1.
	"""
	if n == 0:
		return 1  # Base case: the factorial of 0 is defined as 1
	else:
		return n * factorial(n-1)  # Recursive case: n * (n-1)!

# Main execution: Get the number from command-line arguments and print its factorial
f = factorial(int(sys.argv[1]))  # Convert input to an integer and compute the factorial
print(f)  # Print the computed factorial
