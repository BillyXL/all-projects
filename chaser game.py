import random
import time
from time import sleep
import sys

lifecounter = 1



print("welcome to the chaser game,")
sleep(2)
print("-")
sleep(0.5)
print("-")
sleep(0.25)
print("you will be asked a series of questions, get one wrong,")
sleep(1)
print("-----")
sleep(0.3)
print("-----")
sleep(0.3)
print("and the chaser gets you")
sleep(0.5)
print("-----")
sleep(0.5)
print("-----")
sleep(0.5)
print("now choose your difficulty, 1 life, 2 lives, or 3 lives, please type 1,2 or 3")
chosenlives =int(input())

if chosenlives == 1:
    lifecounter = 1
elif chosenlives == 2:
    lifecounter = 2
elif chosenlives == 3:
    lifecounter = 3
else:
    sys.exit("don't try be funny buddy, game over")



answer1 = "4"
answer2 = "100"
answer2_5 = ""
answer3 = "13"
answer4 = "81pi"
answer5 = "i"


sleep(0.5)
print("-----")
sleep(0.5)
print("-----")
sleep(0.5)
guess1 = input("what's 2 + 2?")
sleep(0.5)
print("-----")
sleep(0.5)
print("-----")
sleep(0.5)


if guess1 == answer1 :
    print("CORRECT!")

else :
    lifecounter = lifecounter - 1
    print("incorrect, minus one life, you have:",lifecounter, "lives remaining")
if lifecounter == 0:
    print("game over")
    sleep(1)
    sys.exit("better luck next time")
    sleep(0.5)
    print("-----")
    sleep(0.5)
    print("-----")
    sleep(0.5)

guess2 = input("what is 10 x 10 ?")

if guess2 == answer2:
    print("CORRECT!")
else:
    lifecounter = lifecounter - 1
    print("incorrect, you now have:", lifecounter, "lives remaining")

if lifecounter == 0:
    print("game over")
    sleep(1)
    sys.exit("better luck next time")
    
guess2_5 = input("what 167 + 244?")

if guess2_5 == answer2_5:
    print("CORRECT!")
else:
    lifecounter = lifecounter - 1
    print("incorrect, you now have:",lifecounter,"lives remaining")
    
sleep(0.5)
print("-----")
sleep(0.5)
print("-----")
sleep(0.5)
guess3 = input("what is the square root of 269?")
sleep(0.5)
print("-----")
sleep(0.5)

if guess3 == answer3 :
    print("correct")
else:
    lifecounter = lifecounter - 1
    print("incorrect, you now have:",lifecounter,"lives left" )
    sleep(0.5)
if lifecounter == 0:
    print("game over")
    sleep(1)
    sys.exit("better luck next time")

print("-----")
sleep(0.5)
print("-----")
sleep(0.5)
guess4 = input("what is the area of a circle with a diameter of 9cm, in termns of pi (e.g. 61pi) ")
sleep(0.5)
print("-----")
sleep(0.5)
print("-----")
sleep(0.5)

if guess4 == answer4 :
    print("CORRECT!")

else:
    lifecounter = lifecounter - 1
    print("incorrect, you now have:",lifecounter,"lives remaining")

if lifecounter == 0:
    print("game over")
    sleep(1)
    sys.exit("better luck next time")

sleep(0.5)
print("-----")
sleep(0.5)
guess5 = input("is the square root of -1?")
sleep(0.5)
print("-----")
sleep(0.5)

if answer5 == guess5:
    print("CORRECT!")
else:
    lifecounter = lifecounter - 1
    print("incorrect, you now have:",lifecounter,"lives remaining")
if lifecounter == 0:
    print("game over")
    sleep(1)
    sys.exit("better luck next time")

print("congrats on beating the game, play again on a higher difficulty or try make a freind do it") 
sys.exit()