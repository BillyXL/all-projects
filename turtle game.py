#imports

import turtle as t
from turtle import *
import colorsys as c
import sys as s
import random
import time
from time import sleep


speed = int(input("how fast should the turtle go (1-10)"))
t.speed(speed)
width = int(input("How wide should your drawing be?(1-10)"))
t.width(width)
R = float(input("what is red value?(0-255)"))
B = float(input("what is blue value?(0-255)"))
G = float(input("what is green value?(0-255)"))

print(R,G,B)
t.bgcolor("grey")
print(R,G,B)
t.hideturtle()
t.setup(1000,1000)

x = 0
t.color(c.hsv_to_rgb(R,G,B))
t.right(90)
t.circle(200,360)

while x >= -1:
    t.goto(random.randint(-500,500),random.randint(-500,500))
    y = random.randint(5,100)
    t.begin_fill()
    t.down()
    t.setheading(90)
    t.forward(y)
    t.setheading(180)
    t.forward(y)
    t.setheading(270)
    t.forward(y)
    t.setheading(0)
    t.forward(y)
    t.end_fill()
    t.up()
    z = random.randint(5,100)
    t.goto(random.randint(-500,500),random.randint(-500,500))
    t.begin_fill()
    t.circle(z)
    t.end_fill()
    
    
while z >= -1:
    z = random.randint(5,100)
    t.goto(z)
    t.down()
    t.begin_fill()
    t.circle(z)
    t.end_fill()
    t.up()