#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    LastD = (number * -1) % 10
    if LastD != 0:
        LastD *= -1
else:
    LastD = number % 10
if LastD == 0:
    print("Last digit of {:d}".format(number), end="")
    print(" is {:d} and is 0".format(LastD))
elif LastD < 6:
    print("Last digit of {:d}".format(number), end="")
    print(" is {:d} and is less than 6 and not 0".format(LastD))
if LastD > 5:
    print("Last digit of {:d}".format(number), end="")
    print(" is {:d} and is greater than 5".format(LastD))
