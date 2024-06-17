from tkinter  import *
root=Tk()
canvas_width =800
canvas_height =400

root.geometry(f'{canvas_width}x{canvas_height}')
root.title("My Canvas Drawing")

canwidget=Canvas(root,width=canvas_width, height=canvas_height)
canwidget.pack()
canwidget.create_line(0,0,800,400,fill='blue')
canwidget.create_line(0,400,800,0,fill='blue')

canwidget.create_arc(0,5,70,200)
root.mainloop()