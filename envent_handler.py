from tkinter import *
window=Tk()
window.title
window.geometry('100x100')

def handle_keypress(event):
    """Print The charcter assciated to the key pressed"""
    print(event.char)

window.bind("<Key>" ,handle_keypress)

def handle_click(event):
    print('\nThe button was clicked!')

button = Button(text='Click me!')
button.pack()

button.bind('<Button-1>', handle_click)

window.mainloop()