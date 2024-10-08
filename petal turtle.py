import turtle as t
from turtle import *
import colorsys as c
import sys as s

t.hideturtle()
t.setup(800,800)
t.speed(0)
t.width(2)
t.bgcolor("black")
for j in range(25):
    for i in range(15):
        t.color(c.hsv_to_rgb(i/15,j/25,1))
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(180)
        t.circle(50,24)

sys.exit()