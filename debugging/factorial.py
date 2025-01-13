#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to eventually exit the loop
    return result

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except IndexError:
    print("Please provide a number as a command-line argument.")
except ValueError:
    print("The provided argument must be a valid integer.")
