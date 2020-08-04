import tkinter as tk
from PIL import ImageTk,Image


window = tk.Tk()
window.title("Frame")
window.iconbitmap("assets/1.ico")

frame = tk.LabelFrame(window, padx=50, pady=50)
frame.pack(padx=10, pady=10)

button1 = tk.Button(frame, text="Nie klikaj")
button2 = tk.Button(frame, text="Nie klikaj też tutaj")
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)




window.mainloop()