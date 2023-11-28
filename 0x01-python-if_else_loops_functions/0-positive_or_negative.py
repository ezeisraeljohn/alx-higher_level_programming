#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Condition to check positive or negative value
if number > 0:
    print(f"{number} is positive")  # print this if number is positive
elif number == 0:
    print(f"{number} is zero")  # print this if number is zero
else:
    print(f"{number} is negative")  # print this if number is negative
