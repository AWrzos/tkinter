import tkinter as tk
from PIL import ImageTk,Image


window = tk.Tk()
window.title("Aplikacja")
window.iconbitmap("assets/1.ico")

def open():
    top = tk.Toplevel()
    top.title("Drugie okno")
    top.iconbitmap("assets/1.ico")
    global my_image
    my_image = ImageTk.PhotoImage(Image.open("assets/2.jpg"))
    my_label = tk.Label(top, image=my_image).pack()
    button2 = tk.Button(top, text="Zamknij to okno", command=top.destroy).pack()




button = tk.Button(window, text="Otwiera drugie okno", command=open).pack()




window.mainloop()