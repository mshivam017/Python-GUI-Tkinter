from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry('700x400')
root.iconbitmap('selffo.ico')

Ready_label = Label(text='Ready',bg='blue', fg='white', font='comicsansms 19 bold', padx=100, pady=10)
Ready_label.pack(side='bottom',fill=X)
root.mainloop()