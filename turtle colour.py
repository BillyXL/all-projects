import turtle

hz = turtle.turtle()
hz.speed(50)
hz.shape("cat")
hz.color('red','yellow')

cl = ['red','green','blue']
hz.speed(50)
def drawArt(angle,d,x,y):
    
    hz.up()
    hz.goto(x,y)
    hz.down()
    c = 0
    for i in range(1,400):
        hz.pencolour(cl[c])
        hz.forward(d)