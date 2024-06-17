from tkinter import Label,Button,Tk
from PIL import Image, ImageTk
root = Tk()
root.title("My Button Widget")
root.geometry("600x300")

def hii():
    print("Hello, Welcome to Tkinter")

def name():
    print("Hi, My Name is Shivam")

btn2 = Button(text='Click Me', bg='#55719e',highlightthickness=8,pady=10,state="active",cursor="cross",command=name)
btn2.pack(pady=20)


first_Img = Image.open('shiva.jpg')
first_Img_Resize = first_Img.resize((250, 120))
first_Img_filter = ImageTk.PhotoImage(first_Img_Resize)
# img= Label(image=first_Img_filter,height=100, width=80)
# img.pack()
btn2 = Button(image=first_Img_filter, bg='#ff719a',highlightthickness=8,pady=10,cursor="hand2",command=hii)
btn2.pack()

btn3 = Button(image=first_Img_filter, bg='#ff719a',highlightthickness=8,pady=10,cursor="hand2")
btn3.pack()

btn3 = Button(image=first_Img_filter, bg='#ff719a',highlightthickness=8,pady=10,cursor="hand2",command=hii)
btn3.pack()

root.mainloop()