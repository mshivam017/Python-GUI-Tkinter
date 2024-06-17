from tkinter import *
root = Tk()
root.geometry('500x300')
def form_data_store():
    print(f"[{user_name_store.get()},{contact_store.get()},{pincode_store.get()},{address_store.get()},{password_store.get()},{Agreement_check.get()}]\n")

    with open('record.txt','a') as f:
        f.write(f"[{user_name_store.get()},{contact_store.get()},{pincode_store.get()},{address_store.get()},{password_store.get()},{Agreement_check.get()}]\n")


frame = Frame(root).grid(padx=50,pady=50)

user_name = Label(frame,text='Name: ').grid(row=1,column=3)
contact = Label(frame,text='Contact: ').grid(row=2,column=3)
pincode = Label(frame,text='Pincode: ').grid(row=3,column=3)
address = Label(frame,text='Address: ').grid(row=4,column=3)
password = Label(frame,text='Password: ').grid(row=5,column=3)

user_name_store = StringVar()
contact_store   = IntVar()
pincode_store   = IntVar()
address_store   = StringVar()
password_store  = StringVar()
Agreement_check = BooleanVar()

user_name_entry = Entry(frame,textvariable=user_name_store).grid(row=1,column=5)
contact_entry   = Entry(frame,textvariable=contact_store).grid(row=2,column=5)
pincode_entry   = Entry(frame,textvariable=pincode_store).grid(row=3,column=5)
address_entry   = Entry(frame,textvariable=address_store).grid(row=4,column=5)
password_entry  = Entry(frame,textvariable=password_store,show='*').grid(row=5,column=5)
check_agreement_entry  = Checkbutton(frame,text="Agree or not?",variable=Agreement_check).grid(row=6,column=5)
submit_button = Button(frame,text="Submit",cursor="hand2",command=form_data_store).grid(row=7,column=5)

root.mainloop()