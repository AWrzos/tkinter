import tkinter as tk

window = tk.Tk()
window.title("Kalkulator")

entry = tk.Entry(window, width= 35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = tk.Button(window, text="1", padx=40, pady=20)
button_2 = tk.Button(window, text="2", padx=40, pady=20)
button_3 = tk.Button(window, text="3", padx=40, pady=20)
button_4 = tk.Button(window, text="4", padx=40, pady=20)
button_5 = tk.Button(window, text="5", padx=40, pady=20)
button_6 = tk.Button(window, text="6", padx=40, pady=20)
button_7 = tk.Button(window, text="7", padx=40, pady=20)
button_8 = tk.Button(window, text="8", padx=40, pady=20)
button_9 = tk.Button(window, text="9", padx=40, pady=20)
button_0 = tk.Button(window, text="0", padx=40, pady=20)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)




window.mainloop()