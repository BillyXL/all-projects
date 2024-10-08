import time
from time import sleep
import _thread
import random


def new_thread():
    
    print("type for v-bucks")
    inpuT = input()
    if input != "ufkjnhhh":
        print("successful")
    sleep(1)
        

    
second_thread = _thread.start_new_thread(new_thread, ())

while True:            
    new_thread()
    print("hello")
    sleep(1)