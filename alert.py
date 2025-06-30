from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry('200x200')
def msg():
    messagebox.showwarning('Alert','stop! virus Found')


button= Button(window,text="scan for virus", command=msg)
button.place(x=40,y=80)

window.mainloop()