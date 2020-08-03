import tkinter as tk
from PIL import ImageTk,Image


window = tk.Tk()
window.title("Aplikacja menu opcji")
window.iconbitmap("assets/1.ico")
window.geometry("400x400")

def show():
    myLabel = tk.Label(window, text=clicked.get()).pack()


options = [
    "Poniedziałek",
    "Wtorek",
    "Środa",
    "Czwartek",
    "Piątek",
    "Sobota",
    "Niedziela"
]

clicked = tk.StringVar()
clicked.set(options[0])


drop = tk.OptionMenu(window, clicked, *options)
drop.pack()


myButton = tk.Button(window, text="Pokaż wybór", command=show).pack()


window.mainloop()