from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title("My GUI Screen")
root.iconbitmap('selffo.ico')
root.geometry("600x400")
root.minsize(200,100)
root.maxsize(1280,720)

var_text = Label(text='Lucky is a Good Boy and this is his GUI interface')
var_text.pack()
#for image
# shiva_photo = PhotoImage(file='1.png')
# var_Label = Label(image=shiva_photo)

image = Image.open('shiva.jpg')
photo = ImageTk.PhotoImage(image)
var_Label = Label(image=photo)

var_Label.pack()
# end for image is label pack

root.mainloop()
