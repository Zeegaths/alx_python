#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
#print("Last digit of {} is {}".format(number, last_digit)) 
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif number < 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, -last_digit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))