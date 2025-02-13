from turtle import *
t = Turtle()
# this is my best star i could make.
def star():
    t.left(60)
    t.forward(12.5)
    t.right(120)
    t.forward(12.5)
    t.right(150)
    t.forward(15)
    t.right(150)
    t.forward(12.5)
    t.right(150)
    t.forward(15)
    t.penup()

def moon():
    t.circle(100)
    t.penup()

def star_2000():
    for i in range(2000):
        star()
        t.penup()
        t.goto(10*i,10*i)
        t.pendown()

star_2000()
t.penup()
t.goto(-200,0)
t.pendown()
moon()
done()