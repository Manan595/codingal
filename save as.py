from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename


window = Tk()
window.geometry('600x500')
window.title('codingal text editor')
window.rowconfigure(0,minsize=800, weight=1)

def open_file():
    """open a file for editing"""
    filepath= askopenfilename(filetypes=[('Text files','*.txt'),('all files','*.*')])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath,'r')as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title('codingal text editor - {filepath}')

def save_file():
    filepath= asksaveasfilename(defaultextension='txt',filetypes=[('text files',"*.txt"),('all files','*.*')])
    if not filepath:
        return
    with open(filepath,'w') as output_file:
         text= txt_edit.get(1.0,END)
         output_file.write(text)
         window.title('codingal text editor - {filepath}')
txt_edit = Text(window)
fr_buttons=Frame(window, relief=RAISED, bd=2)
btn_open= Button(fr_buttons,text='Open',command=open_file)
btn_save= Button(fr_buttons,text="save as...",command=save_file)

btn_open.grid(row=0)