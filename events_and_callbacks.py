import tkinter as tk

def on_left_click(event):
    print("Left mouse button clicked at", event.x, event.y)

def on_key_press(event):
    print("Key pressed:", event.char)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

# Binding mouse click event
canvas.bind("<Button-1>", on_left_click)

# Binding key press event
root.bind("<KeyPress>", on_key_press)

root.mainloop()
