import tkinter as tk
from PIL import ImageTk,Image

window = tk.Tk()
window.title("Aplikacja do przeglądania zdjęć")
window.iconbitmap("assets/1.ico")

my_image1 = ImageTk.PhotoImage(Image.open("assets/2.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("assets/3.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("assets/4.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("assets/5.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("assets/6.jpg"))
my_image6 = ImageTk.PhotoImage(Image.open("assets/7.jpg"))
my_image7 = ImageTk.PhotoImage(Image.open("assets/8.jpg"))

image_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6, my_image7]

status = tk.Label(window, text="Image 1 of " + str(len(image_list)), bd=1, relief=tk.SUNKEN, anchor=tk.E)

my_label = tk.Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = tk.Label(image=image_list[image_number-1])
    button_forward = tk.Button(window, text=">>", command=lambda: forward(image_number+1))
    button_back = tk.Button(window, text="<<", command=lambda: back(image_number-1))

    if image_number == 7:
        button_forward = tk.Button(window, text=">>", state=tk.DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    status = tk.Label(window, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=tk.SUNKEN, anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = tk.Label(image=image_list[image_number - 1])
    button_forward = tk.Button(window, text=">>", command=lambda: forward(image_number + 1))
    button_back = tk.Button(window, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = tk.Button(window, text="<<", state=tk.DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    status = tk.Label(window, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=tk.SUNKEN, anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

button_back = tk.Button(window, text="<<",command=back, state=tk.DISABLED)
button_forward = tk.Button(window, text=">>", command=lambda: forward(2))
button_quit = tk.Button(window, text="Exit program", command=window.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

window.mainloop()