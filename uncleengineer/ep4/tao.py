import turtle
import random

turtle.bgcolor('black')
color = ['red','yellow','blue','green']

tao = turtle.Pen()
tao.shape('turtle')

for i in range(10):
    tao.circle(50)
    cl= random.choice(color)
    tao.color(cl)
    tao.left(30)