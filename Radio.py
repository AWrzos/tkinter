import tkinter as tk
from PIL import ImageTk,Image

window = tk.Tk()
window.title("Pizza")
window.iconbitmap("assets/1.ico")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Ser", "Ser"),
    ("Pieczarki", "Pieczarki"),
    ("Cebula", "Cebula"),
]
pizza = tk.StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    tk.Radiobutton(window, text=text, variable=pizza, value=mode).pack(anchor=tk.W)

def clicked(value):
    myLabel = tk.Label(window, text=value)
    myLabel.pack()

myButton = tk.Button(window, text="Dodaj", command=lambda: clicked(pizza.get()))
myButton.pack()

window.mainloop()