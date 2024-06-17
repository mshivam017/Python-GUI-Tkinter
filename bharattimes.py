from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title('BHARAT GLOBAL TIMES')
root.iconbitmap('selffo.ico')
root.geometry('1280x720')
#frame1
f1 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
Label(f1,text='''A day after Prime Minister Narendra Modi told Ukraine President VolodymyrZelenskyy that India continues to encourage a peaceful resolution of the Russia-Ukraine conflict through dialogue and diplomacy, New Delhi sent a senior official to Switzerland for the two-day Summit on Peace in Ukraine that began  Saturday. We can configure the Text widget properties such as its font properties, text color, background, etc., by using the configure() method. To set the justification of our text inside the Text widget, we can use tag_add() and tag_configure() properties. We will specify the value of "justify" as CENTER.''',pady=22,justify="left",wraplength=1200).pack(side="left")

first_Img = Image.open('shiva.jpg')
first_Img_Resize = first_Img.resize((250, 120))
first_Img_filter = ImageTk.PhotoImage(first_Img_Resize)
Label(f1,image=first_Img_filter,height=100, width=80).pack(side="right")

f1.pack(anchor='nw',fill=X)

# frame2
f2 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
Label(f2,text='''"Kate to have you back," says the Sunday Mirror. It says a "radiant" Princess of Wales brought sunshine to a rainy parade, adding that thousands "braved wet weather to cheer the mum of three" at her first public appearance since her diagnosis.

The Sunday Express is similar in its praise for what it calls her "spectacular" return. The paper goes on to say that the King, who also has cancer, and his daughter-in-law stood side-by-side on the balcony "as a striking symbol of unity and defiance against the disease".
The Observer leads with what it calls a "bleak" verdict by the health think tank, the Nuffield Trust, of the Labour and Conservative manifesto commitments on NHS funding.''',pady=22,justify="left",wraplength=1200).pack(side="left")

sec_Img = Image.open('plant.jpg')
sec_Img_Resize = sec_Img.resize((250, 120))
sec_Img_filter = ImageTk.PhotoImage(sec_Img_Resize)
Label(f2,image=sec_Img_filter,height=100, width=80).pack(side="right")

f2.pack(anchor='nw',fill=X)


# frame3
f3 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
Label(f3,text='''The Sunday Times carries what it describes as a "highly personal interview" with Rishi Sunak. He reveals how he draws strength from his Hindu faith to cope with the pressures of the "bruising general election campaign".
The paper says he rejects accusations that Liz Truss is to blame for the Conservative party’s performance in opinion polls. Mr Sunak tells the Sunday Times: "I’m ultimately responsible for what I’m doing and no one else is. It rests on my shoulders.”''',pady=22,justify="left",wraplength=1200).pack(side="left")

f3_Img = Image.open('cloth-1.jpg')
f3_Img_Resize = f3_Img.resize((250, 120))
f3_Img_filter = ImageTk.PhotoImage(f3_Img_Resize)
Label(f3,image=f3_Img_filter,height=100, width=80).pack(side="right")

f3.pack(anchor='nw',fill=X)


# frame4
f4 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
Label(f4,text='''A government-owned national daily founded in 1703 in Vienna, Austria, Wiener Zeitung had faced the possibility of closure for most of this century. In October 2022, the threat was realised when a new law was adopted by the Austria parliament that effectively cut off the main revenue stream of what was the official government gazette until 2020.

Government job ads and companies’ annual financial results – required by law to be published in the paper – had largely funded WZ’s roughly €20-million annual revenue.

That would be stripped away by the end of 2022.

This led to, arguably, the fastest, most radical transformation in newsroom history. “It was super quick; we had to do it in no time,” acknowledges editor-in-chief, Katharina Schmidt.''',pady=22,justify="left",wraplength=1200).pack(side="left")

f4_Img = Image.open('anime-girl-1.jpg')
f4_Img_Resize = f4_Img.resize((250, 120))
f4_Img_filter = ImageTk.PhotoImage(f4_Img_Resize)
Label(f4,image=f4_Img_filter,height=100, width=80).pack(side="right")

f4.pack(anchor='nw',fill=X)


# frame5
f5 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
Label(f5,text='''A day after Prime Minister Narendra Modi told Ukraine President VolodymyrZelenskyy that India continues to encourage a peaceful resolution of the Russia-Ukraine conflict through dialogue and diplomacy, New Delhi sent a senior official to Switzerland for the two-day ''',pady=22,justify="left",wraplength=1200).pack(side="left")

f5_Img = Image.open('car-1.jpg')
f5_Img_Resize = f5_Img.resize((250, 120))
f5_Img_filter = ImageTk.PhotoImage(f5_Img_Resize)
Label(f5,image=f5_Img_filter,height=100, width=80).pack(side="right")

f5.pack(anchor='nw',fill=X)


# frame6
f6 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
Label(f6,text='''A day after Prime Minister Narendra Modi told Ukraine President VolodymyrZelenskyy that India continues to encourage a peaceful resolution of the Russia-Ukraine conflict through dialogue and diplomacy, New Delhi sent a senior official to Switzerland for the two-day Summit on Peace in Ukraine that began  Saturday. We can configure the Text widget properties such as its font properties, text color, background, etc., by using the configure() method. To set the justification of our text inside the Text widget, we can use tag_add() and tag_configure() properties. We will specify the value of "justify" as CENTER.''',pady=22,justify="left",wraplength=1200).pack(side="left")

f6_Img = Image.open('shiva.jpg')
f6_Img_Resize = f6_Img.resize((250, 120))
f6_Img_filter = ImageTk.PhotoImage(f6_Img_Resize)
Label(f6,image=f6_Img_filter,height=100, width=80).pack(side="right")

f6.pack(anchor='nw',fill=X)


# frame7
f7 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
Label(f7,text='''A day after Prime Minister Narendra Modi told Ukraine President VolodymyrZelenskyy that India continues to encourage a peaceful resolution of the Russia-Ukraine conflict through dialogue and diplomacy, New Delhi sent a senior official to Switzerland for the two-day Summit on Peace in Ukraine that began  Saturday. We can configure the Text widget properties such as its font properties, text color, background, etc., by using the configure() method. To set the justification of our text inside the Text widget, we can use tag_add() and tag_configure() properties. We will specify the value of "justify" as CENTER.''',pady=22,justify="left",wraplength=1200).pack(side="left")

f7_Img = Image.open('shiva.jpg')
f7_Img_Resize = f7_Img.resize((250, 120))
f7_Img_filter = ImageTk.PhotoImage(f7_Img_Resize)
Label(f7,image=f7_Img_filter,height=100, width=80).pack(side="right")

f7.pack(anchor='nw',fill=X)


# frame8
# f8 = Frame(root,height=200,borderwidth=6,relief=SUNKEN)
# Label(f8,text='''A day after Prime Minister Narendra Modi told Ukraine President VolodymyrZelenskyy that India continues to encourage a peaceful resolution of the Russia-Ukraine conflict through dialogue and diplomacy, New Delhi sent a senior official to Switzerland for the two-day Summit on Peace in Ukraine that began  Saturday. We can configure the Text widget properties such as its font properties, text color, background, etc., by using the configure() method. To set the justification of our text inside the Text widget, we can use tag_add() and tag_configure() properties. We will specify the value of "justify" as CENTER.''',pady=22,justify="left",wraplength=1200).pack(side="left")

# f8_Img = Image.open('shiva.jpg')
# f8_Img_Resize = f8_Img.resize((250, 120))
# f8_Img_filter = ImageTk.PhotoImage(f8_Img_Resize)
# Label(f8,image=first_Img_filter,height=100, width=80).pack(side="right")

# f8.pack(anchor='nw',fill=X)

root.mainloop()