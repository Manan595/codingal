from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('dennomination counter')
root.configure(bg='light blue')
root.geometry('650x400')
upload = Image. open('app_img.jpg')
upload= upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root, image=image, bg='light blue')
label.place(x=180,y=20)
label1=label(root,text='Hey user! Welcome to denomination conter aplication',bg='light blue')
label1.place(relx=0.5,y=340, anchor=CENTER)

def topwin():
    top=Toplevel()
    top.title('dennomination counter')
    top.configure('light grey')
    top.geometry('600x500+50+50')
    
    label= Label(top, text="enter total amount",bg='light grey')
    enter=Entry(top)
    lbl=Label(top,text="here are the number of notes in each dennomination",bg='light grey')

   
    l1= Label(top,text="2000",bg='light grey')
    l2= Label(top,text="500",bg='light grey')
    l3= Label(top,text="100",bg='light grey')

    t1=