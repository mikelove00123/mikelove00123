from tkinter import *
from tkinter import ttk

def calprofit():
    at = alltank.get()
    print("This is a function")


GUI = Tk()
GUI.geometry("500x600")
GUI.title("Mike Calculator")

#botton 1 is old botton
'''
BCal = Button(GUI, text='Calculate')
BCal.pack()'''

#text box for enter the value
#StringVar is a bax that can flexible value
alltank=StringVar()
Etank = ttk.Entry(GUI,textvariable=alltank,font=('Augsana New',20))
Etank.pack()

#botton 2 is new botton
BCal2 = Button(GUI, text='New Calculate',command=calprofit)
BCal2.pack(ipadx=20,ipady=10)

GUI.mainloop()