from ball import *
from graphics import *

bs = []
for i in range(0,10):
    bs.append(Ball())

win = GraphWin("Hello",500,500)

for i in range(0,10):
    bs[i].draw(win)
