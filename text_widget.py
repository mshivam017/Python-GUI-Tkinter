from tkinter import Text,Tk
root = Tk()
root.geometry('400x400')

text_widget = Text(root,bg='red',width=50 , height=50).pack()
root.mainloop()