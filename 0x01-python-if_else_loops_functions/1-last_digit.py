#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if lastDigit > 5:
	print("the Last digit of {} is {} and is greater than 5".format(number,lastDigit))
elif lastDigit == 0: 
	print("the Last digit of {} is {} ".format(number,lastDigit))
elif lastDigit < 6 and lastDigit != 0: 
	print("the Last digit of {} is -{} and is less than 6 and not 0".format(number,lastDigit))
