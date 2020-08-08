from tkinter import *
from PIL import ImageTk,Image
import sqlite3


window = Tk()
window.title("Aplikacja bazy danych")
window.iconbitmap("assets/1.ico")
window.geometry("400x400")

# Tworzenie bazy danych lub połączenie do istniejącej
conn = sqlite3.connect("address_book.db")

# Tworzenie kursora
c = conn.cursor()

# Stworzenie tabeli
# c.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         zipcode integer
#         )""")

# Stworzenie funkcji do usuwania rekordów
def delete():
    # Tworzenie bazy danych lub połączenie do istniejącej
    conn = sqlite3.connect("address_book.db")

    # Tworzenie kursora
    c = conn.cursor()


    # Usuwanie rekordu
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())


    # Zatwierdzenie zmian
    conn.commit()

    # Zamykanie połączenia z bazą danych
    conn.close()





# Stworzenie funkcji submit
def submit():
    # Tworzenie bazy danych lub połączenie do istniejącej
    conn = sqlite3.connect("address_book.db")

    # Tworzenie kursora
    c = conn.cursor()


    # Dodanie do tabeli
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :zipcode) ",
              {
                  "f_name" : f_name.get(),
                  "l_name" : l_name.get(),
                  "address" : address.get(),
                  "city" : city.get(),
                  "zipcode" : zipcode.get()
              })

    # Zatwierdzenie zmian
    conn.commit()

    # Zamykanie połączenia z bazą danych
    conn.close()

    # Wyczyszczenie pola tekstowego
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

# Stworzenie funkcji przeszukania bazy danych
def query():
    # Tworzenie bazy danych lub połączenie do istniejącej
    conn = sqlite3.connect("address_book.db")

    # Tworzenie kursora
    c = conn.cursor()

    # Przeszukanie bazy danych
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[5]) + "\n"

    query_label = Label(window, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)




    # Zatwierdzenie zmian
    conn.commit()

    # Zamykanie połączenia z bazą danych
    conn.close()


# Stworzenie pól tekstowych
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(window, width=30)
l_name.grid(row=1, column=1)
address = Entry(window, width=30)
address.grid(row=2, column=1)
city = Entry(window, width=30)
city.grid(row=3, column=1)
zipcode = Entry(window, width=30)
zipcode.grid(row=4, column=1)
delete_box = Entry(window, width=30)
delete_box.grid(row=8, column=1, pady=5)


# Stworzenie etykiet do pól tekstowych
f_name_label = Label(window, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(window, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(window, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(window, text="City")
city_label.grid(row=3, column=0)
zipcode_label = Label(window, text="Zipcode")
zipcode_label.grid(row=4, column=0)
delete_box_label = Label(window, text="Numer ID do usunięcia")
delete_box_label.grid(row=8, column=0, pady=5)

# Stworzenie przycisków zatwierdzania
submit_button = Button(window, text="Dodaj rekord do bazy danych", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Stworzenie przycisku przeszukania bazy danych
query_btn = Button(window, text="Pokaż rekordy", command=query)
query_btn.grid(row=6,column=0, columnspan=2, pady=10, padx=10, ipadx=140)

# Stworzenie przycisku do usuwania
delete_btn = Button(window, text="Usuń rekord", command=delete)
delete_btn.grid(row=9,column=0, columnspan=2, pady=10, padx=10, ipadx=145)


# Zatwierdzenie zmian
conn.commit()


# Zamykanie połączenia z bazą danych
conn.close()

window.mainloop()