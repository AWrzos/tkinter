import tkinter as tk
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt



window = tk.Tk()
window.title("Wykresy")
window.iconbitmap("assets/1.ico")
window.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 15)
    plt.show()


my_button = tk.Button(window, text="Narysuj histogram", command=graph)
my_button.pack()

window.mainloop()