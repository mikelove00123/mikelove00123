from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def calprofit():
    at = int(alltank.get())
    cal_sell = at*30
    cal_cost = at*20
    profit = cal_sell-cal_cost
    relex = profit/350000
    textshow = 'i have profit: {:,d} million\n'.format(profit)
    textshow2 = "you can buy relex: {} peices".format(relex)
    messagebox.showinfo('My Profit: ',textshow+textshow2)

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