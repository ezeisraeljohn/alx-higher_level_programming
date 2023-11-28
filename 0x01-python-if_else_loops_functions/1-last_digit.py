#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = number % 10

# first string to be concatinated with the conditioned string
pre_string = f"Last digit of {number} is {last_digit} "

# Conditioned string
if last_digit > 5:
    print(pre_string + "and is greater than 5")
elif last_digit == 0:
    print(pre_string + "and is 0")
elif last_digit < 6 and last_digit != 0:
    print(pre_string + "and is less than 6 and not 0")
