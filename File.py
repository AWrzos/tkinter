import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog

window = tk.Tk()
window.title("Aplikacja")
window.iconbitmap("assets/1.ico")
window.geometry("600x600")


def open():
    global my_image
    window.filename = filedialog.askopenfilename(initialdir="E:/Arti/pajton/images", title="Wybierz plik",
                                                 filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    my_label = tk.Label(window, text=window.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(window.filename))
    my_image_label = tk.Label(image=my_image).pack()


my_button = tk.Button(window, text="Otwórz plik", command=open).pack(padx=10, pady=10)


window.mainloop()