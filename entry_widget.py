from tkinter import Tk, Entry,Frame
root = Tk()
root.title("My Entry Widget")
f1= Frame(root,bg='green',padx=400,pady=100)
f1.pack()
e1 = Entry(f1,bg='light blue',bd=4,relief='sunken',show='*', width=100,state="normal")
e1.pack()

root.mainloop()