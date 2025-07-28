import tkinter as tk
from tkinter import ttk, messagebox

class restraunatmanagement:
    def __init__(self,root):
        self.root= root
        self.root.title('restraunt management app')


        self.menue_items={
            'fries meal':2,
            'lunch meal':2,
            'burger meal':3,
            'pizza meal':4,
            'chese burger':2.5,
                    'drinks':1                                                                                                                                                           
}
        self.exchange_rate=82
        self.setup_baground(root)
        frame = ttk.frame(root)
        frame.place=(relx=0, rely=0.5, anchor=tk.CENTER)
        ttk.label(frame,text='restraunt order management',font=('Arial',20,'bold')).grid(row=0,columnspan=3,padyx=10,padyy=10)

        self.menue_items={}
        self.menue_quantites={}

        for i, (item,price) in enumerate(self.menue_items.items(),start=1):
            label=ttk.Label(frame, text=f'{item}(${price}):',fount=('arial',12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menue_items[item]=label

            quantity_entry = ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menue_quantites[item]
