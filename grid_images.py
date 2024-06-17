import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("720x500")
root.title("Display Images using Grid Function")
image1 = Image.open(r"shiva.jpg")
image1 = image1.resize((240, 240))
image1 = ImageTk.PhotoImage(image1)

image2 = Image.open(r"shiva.jpg")
image2 = image2.resize((240, 240))
image2 = ImageTk.PhotoImage(image2)

image3 = Image.open(r"shiva.jpg")
image3 = image3.resize((240, 240))
image3 = ImageTk.PhotoImage(image3)

image4 = Image.open(r"shiva.jpg")
image4 = image4.resize((240, 240))
image4 = ImageTk.PhotoImage(image4)

label1 = tk.Label(image=image1)
label2 = tk.Label(image=image2)
label3 = tk.Label(image=image3)
label4 = tk.Label(image=image4)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=1)
label4.grid(row=1, column=2)
root.mainloop()