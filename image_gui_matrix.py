from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.iconbitmap('selffo.ico')
root.title('Image GUI Matrix')

text_label = Label(text= 'This Only for Practice Use')
shivam_image_open = Image.open('shiva.jpg')
shivam_image_resize = shivam_image_open.resize((100,100))
shivam_image_filter = ImageTk.PhotoImage(shivam_image_resize)
shivam_photo_label = Label(image=shivam_image_filter)

text_label.pack()
shivam_photo_label.pack()


root.mainloop()