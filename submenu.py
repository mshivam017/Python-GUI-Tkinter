from tkinter import *
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


mainmenu =Menu(root)

mymenu= Menu(mainmenu,tearoff=True)
mymenu.add_command(label='File',command=filefun)
mymenu.add_command(label='Edit',command=editfun)
mymenu.add_command(label='Format',command=formatfun)
mymenu.add_command(label='Insert',command=Insertfun)
mymenu.add_separator()
mymenu.add_command(label='Exit',command=quit)
mainmenu.add_cascade(label='New',menu=mymenu)



mymenu1= Menu(mainmenu,tearoff=False)
mymenu1.add_command(label='File',command=filefun)
mymenu1.add_command(label='Edit',command=editfun)
mymenu1.add_command(label='Format',command=formatfun)
mymenu1.add_command(label='Insert',command=Insertfun)
mymenu1.add_separator()
mymenu1.add_command(label='Exit',command=quit)
mainmenu.add_cascade(label='Editor',menu=mymenu1)

root.config(menu=mainmenu)


root.mainloop()