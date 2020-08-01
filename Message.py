import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

window = tk.Tk()
window.title("Aplikacja popup")
window.iconbitmap("assets/1.ico")
window.geometry("400x400")

def popup():
    response = messagebox.askyesno("Wyskakujące okienko", "Wybierz")
    if response == 1:
        tk.Label(window, text="Kliknąłeś Tak").pack()
    else:
        tk.Label(window, text="Kliknąłeś Nie").pack()



tk.Button(window, text="Wyskakujące okienko", command=popup).pack()



window.mainloop()