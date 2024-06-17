from tkinter import Tk,Menu,Label
root=Tk()
root.geometry('600x388')
def filefun():
    print('File Save/Open')
def editfun():
    print('File Edition')
def formatfun():
    print('File Formatted')
def Insertfun():
    print('File Insert')
mymenu =Menu(root)
mymenu.add_command(label='File',command=filefun)
mymenu.add_command(label='Edit',command=editfun)
mymenu.add_command(label='Format',command=formatfun)
mymenu.add_command(label='Insert',command=Insertfun)
mymenu.add_command(label='Exit',command=quit)
root.config(menu=mymenu)


root.mainloop()