#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number < 0:
    if number > -10:
        if number == 0:
            print(f"Last digit of {number} is {number} and is 0")
        elif number < 5:
            print(f"Last digit of {number} is {number} and is less than 6 and not 0 ")
    elif number <= -10:
        last = number % -10
        if last == 0:
            print(f"Last digit of {number} is {last} and is 0")
        elif last < 5:
            print(f"Last digit of {number} is {last} and is less than 6 and not 0 ")
else:
    last = number % 10
    if last > 5:
        print(f"Last digit of {number} is {last} and is greater than 5 ")
    elif last == 0:
        print(f"Last digit of {number} is {last} and is 0")
    elif last <= 5:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0 ")