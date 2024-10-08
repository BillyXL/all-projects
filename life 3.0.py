#imports
import random as r
import time as t
import sys

#random variable assignments
health = r.randint(50,100)
luck = r.randint(1,100)
height = r.randint(1, 10)
if height <= 2:
    actual_height = "4 foot 5"
elif height <= 4:
    actual_height = "5 foot"
elif height <= 6:
    actual_height = "5 foot 8"
elif height <= 8:
    actual_height = "6 foot 4"
else:
    acutal_height = "7 foot 11"
    
intelligence = r.randint(60,140)

#assignment
name = input("what is your name")
if name == "grahame":
    actual_height = "5 foot 3"
    health = 100
    intelligence = 10
    luck = 10


print(f"welcome {name}, this is a game of life, you are presented with options, and you must choose an option to move forward")
t.sleep(4)
print(f"objective: survive")








