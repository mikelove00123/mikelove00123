from tkinter import * 
from ball import *


window = Tk()
canvas = Canvas(window,width=600,height=600)
canvas.pack()

balls=[]
for i in range(0,10):
    balls.append(Ball())
    which = canvas.create_oval(balls[-1].pos.x,balls[-1].pos.y,
                               balls[-1].pos.x + balls[-1].Size,
                               balls[-1].pos.y + balls[-1].Size,
                               fill='#%02x%02x%02x'%(balls[-1].R,balls[-1].G,balls[-1].B)
                               , tag='rebBall', width=2)

while True:
    for i in range(0,10):
        balls[i].move()
        canvas.move(balls[i].name,balls[i].vel.x,balls[i].vel.y)
    canvas.after(20)
    canvas.update()    
window.mainloop()