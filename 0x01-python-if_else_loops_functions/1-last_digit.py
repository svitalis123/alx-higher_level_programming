#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = str(number)
if int(lastdigit[-1:]) > 5:
  print(f"Last digit of {number} is {lastdigit[-1:]} and is greater than 5")
elif int(lastdigit[-1:])  == 0:
  print(f"Last digit of {number} is {lastdigit[-1:]} and is 0")
elif int(lastdigit[-1:]) < 6 and int(lastdigit[-1:]) != 0:
   print(f"Last digit of {number} is {lastdigit[-1:]} and is less than 6 and not 0")
