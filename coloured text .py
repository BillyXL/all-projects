from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import time
from time import sleep

colorama_init()

red = False
green = False
blue= False
white = False
black = False

print("What do you want to print")
user_input = input()

print("How many times do you want to print it?")
number_of_times = int(input())

print("how long should be inbetween the prints(seconds)")
length = float(input())

print("Do you want your text coloured?")
coloured = input()
if coloured == "yes":
    print("Do you want it red, green, blue, white or black?")
    colour = input()
    if colour == "red":
       red = True
    elif colour == "green":
        green = True
    elif colour == "blue":
        blue = True
    elif colour == "white":
        white = True
    elif colour != "red" or "green" or "blue" or "white":
        print("Colour not available, choose again")
    elif colour == "black":
        black = True
        

else: 
    while number_of_times > 0:
        print(user_input)
        number_of_times = number_of_times - 1
        sleep(length)

if red == True:
    while number_of_times > 0:
        print(f"{Fore.RED}", user_input)
        number_of_times = number_of_times - 1
        sleep(length)

if green == True:
    while number_of_times > 0:
        print(f"{Fore.GREEN}", user_input)
        number_of_times = number_of_times - 1
        sleep(length)

if blue == True:
    while number_of_times > 0:
        print(f"{Fore.BLUE}", user_input)
        number_of_times = number_of_times - 1
        sleep(length)

if white == True:
    while number_of_times > 0:
        print(f"{Fore.WHITE}", user_input)
        number_of_times = number_of_times - 1
        sleep(length)
        
if black == True:
    while number_of_times > 0:
        print(f"{Fore.BLACK}", user_input)
        number_of_times = number_of_times - 1
        sleep(length)

while number_of_times > 0:
    print(user_input)
    number_of_times = number_of_times - 1
    sleep(length)
 


    

