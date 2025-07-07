from tkinter import*

screen= Tk()
screen.title('inches to cm')
lbl=Label(text='inches to cm ')
llbl2=Label(text='enter inches')
input2=Entry()

def math():

    sum1=input2.get()
    sum2= float(sum2)
    sum2= sum2 * 2.54
    textbox.insert(END,sum2)


textbox=Text(height=1)
button=Button(text='convert', command=math)
lbl.pack()
llbl2.pack()
input2.pack()
textbox.pack()
button.pack()
screen.mainloop()