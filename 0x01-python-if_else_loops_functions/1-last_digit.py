#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
final_digit = abs(number) % 10
if number < 0:
    final_digit = -final_digit
print("Last digit of {} is {} and is ".format(number, final_digit), end="")
if final_digit > 5:
    print("greater than 5")
elif final_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
