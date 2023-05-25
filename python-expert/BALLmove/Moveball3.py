from tkinter import * 
from vector import Vector
from ball2 import Ball2
from rect import Rect


window = Tk()
canvas = Canvas(window,width=600,height=600)
canvas.pack()

bs=[]
rs=[]
for i in range(0,10):
    bs.append(Ball2(canvas))
    bs[-1].draw()
for i in range(0,10):
    rs.append(Rect(canvas))
    rs[-1].draw()

while True:
    for i in range(0,len(bs)):
        bs[i].move()
    for i in range(0,len(bs)):
        rs[i].move()
    canvas.after(20)
    canvas.update()    
window.mainloop()