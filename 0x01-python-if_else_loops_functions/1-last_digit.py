#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
final_digit = abs(number) % 10
if number < 0:
    final_digit = -final_digit
print(f"Last digit of {number} is {final_digit} and is ", end="")
if final_digit > 5:
    print("greater than 5")
elif final_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
