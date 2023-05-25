from ball import *

import graphics
import time

bs=[]
win = graphics.GraphWin("Hello",500,500)

c = Circle(Point(100, 100),100)
c.setFill(color_rgb(255,0,0))
c.draw(win)

for i in range(0,10):
    bs.append(Ball())

for i in range(0,10):
    bs[i].draw(win)

while True:

    for i in range(0,10):
        bs[i].move()

    time.sleep(1)
