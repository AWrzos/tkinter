import tkinter as tk
from PIL import ImageTk,Image


window = tk.Tk()
window.title("Aplikacja checkbox")
window.iconbitmap("assets/1.ico")
window.geometry("400x400")

def show():
    myLabel = tk.Label(window, text=var.get()).pack()


var = tk.StringVar()

c = tk.Checkbutton(window, text="Sprawdź to okienko", variable=var, onvalue="Pizza", offvalue="Cheeseburger")
c.deselect()
c.pack()



myButton = tk.Button(window, text="Pokaż wybór", command=show).pack()

window.mainloop()