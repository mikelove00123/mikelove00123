from tkinter import * 


window = Tk()
canvas = Canvas(window,width=400,height=300)
canvas.pack()
x0 = 10
y0 =50
x1 = 60
y1 = 100
i = 0
deltax = 2
deltay = 3
which = canvas.create_oval(x0,y0,x1,y1, fil="red", tag='redBall',width=2)

window.mainloop()