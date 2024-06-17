from tkinter import Tk,Button
root=Tk()
def submitval(event):
    print(f"event x: {event.x} event y: {event.y}")

btn = Button(root,text='Click Here')
btn.pack()
btn.bind('<Button-1>',submitval)
root.mainloop()