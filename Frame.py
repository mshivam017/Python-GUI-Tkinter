from tkinter import *
root=Tk()
root.geometry('600x300')
f1 = Frame(root,width="100px",bg='grey',bd=6, relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
l1 = Label(f1,text="Project Tkinter-Python Module")
l1.pack(pady=122)

f2= Frame(root,height=50,bg='grey',bd=6,relief=SUNKEN)
f2.pack(side=TOP, fill=X)
l2 = Label(f2,text="Welcome To Python")
l2.pack(side=LEFT)
root.mainloop()