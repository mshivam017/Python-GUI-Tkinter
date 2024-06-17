from tkinter import Tk,Label,Grid,Entry,StringVar,Button

def getvals():
    print("Username: ",username.get())
    print('Password: ',user_password.get())

root = Tk()
root.geometry("300x600")
root.title('Selffo | Login')
root.iconbitmap('selffo.ico')

user= Label(root,text='Username: ', font=('Ubuntu', 12),compound="top")
password= Label(root,text='Password: ',font=('Ubuntu', 12))
user.grid(padx=20)
password.grid(row=2)

username= StringVar()
user_password = StringVar()
user_entry=Entry(root,textvariable=username)
user_pass= Entry(root,textvariable=user_password,show='*')
user_entry.grid(padx= 80,row=1)
user_pass.grid(row=3)

submit =Button(root,text='Login', cursor='hand2',command=getvals,fg="white",bg="blue",highlightthickness=4).grid(row=5,pady=10)

root.mainloop()