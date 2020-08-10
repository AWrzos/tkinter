import tkinter as tk
import Thermometer as Therm




term = Therm.Thermometer()

def getAnswer(unit):
        answer["text"] = "Odpowiedź: " + str(term.getTemperature(unit))




window = tk.Tk()
window.title("Kalkulator temperatury")



tk.Label(window, text="Podaj liczbę całkowitą oznaczającą temperaturę oraz wybierz jednostkę podanej temperatury").pack(side=tk.TOP, padx=10, pady=10)

entry = tk.Entry(window, width=10)
entry.pack(side=tk.TOP, padx=10, pady=10)


tk.Button(window, text="Celcjusz", command=lambda: term.setTemperature(int(entry.get()))).pack()
tk.Button(window, text="Kelwin", command=lambda: term.setTemperature(int(entry.get()), "K")).pack()
tk.Button(window, text="Fahrenheit", command=lambda: term.setTemperature(int(entry.get()), "F")).pack()

tk.Label(window, text="Następnie wybierz jednostkę w jakiej chcesz otrzymać temperaturę").pack(side=tk.TOP, padx=10, pady=10)

tk.Button(window, text="Celcjusz", command=lambda: getAnswer("C")).pack()
tk.Button(window, text="Kelwin", command=lambda: getAnswer("K")).pack()
tk.Button(window, text="Fahrenheit", command=lambda: getAnswer("F")).pack()

answer = tk.Label(window, text="Odpowiedź: ")
answer.pack(side=tk.TOP, padx=10, pady=10)


window.mainloop()