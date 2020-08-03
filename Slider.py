import tkinter as tk
from PIL import ImageTk,Image


window = tk.Tk()
window.title("Aplikacja suwak")
window.iconbitmap("assets/1.ico")
window.geometry("400x400")

label = tk.Label(window, text="Ustaw suwaki na wartościach i kliknij przyczisk a okno zmieni swoje rozmiary").pack()


vertical = tk.Scale(window, from_=0, to=800)
vertical.pack()

def slide():
    window.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = tk.Scale(window, from_=0, to=800, orient=tk.HORIZONTAL)
horizontal.pack()


my_button = tk.Button(window, text="Zmień wielkość okna", command=slide).pack()


window.mainloop()