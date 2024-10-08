import random

random = random.randint (1,10)

print("choose a number between 1 to 10")
user_choice = int(input())

if user_choice == random:
    print("correct")
    
else:
    print("wrong")