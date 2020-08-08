from tkinter import *
from PIL import ImageTk, Image
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

# Stworzenie funkcji do zapisu edytowanego rekordu
def update():
    # Tworzenie bazy danych lub połączenie do istniejącej
    conn = sqlite3.connect("address_book.db")

    # Tworzenie kursora
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        zipcode = :zipcode

        WHERE oid = :oid """,
              {"first": f_name_editor.get(),
               "last": l_name_editor.get(),
               "address": address_editor.get(),
               "city": city_editor.get(),
               "zipcode": zipcode_editor.get(),

               "oid": record_id

               })

    # Zatwierdzenie zmian
    conn.commit()

    # Zamykanie połączenia z bazą danych
    conn.close()

    editor.destroy()


# Stworzenie funckji do edycji rekordów
def edit():
    global editor
    editor = Tk()
    editor.title("Edytuj rekord")
    editor.iconbitmap("assets/1.ico")
    editor.geometry("400x300")

    # Tworzenie bazy danych lub połączenie do istniejącej
    conn = sqlite3.connect("address_book.db")

    # Tworzenie kursora
    c = conn.cursor()

    record_id = delete_box.get()

    # Przeszukanie bazy danych
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Stworzenie globalnych zmiennych do pól tekstowych

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global zipcode_editor

    # Stworzenie pól tekstowych
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=4, column=1)

    # Stworzenie etykiet do pól tekstowych
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=4, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        city_editor.insert(0, record[2])
        address_editor.insert(0, record[3])
        zipcode_editor.insert(0, record[4])

    # Stworzenie przycisku do zapisu edytowanych danych
    edit_btn_editor = Button(editor, text="Zapisz rekord", command=update)
    edit_btn_editor.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=142)


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
                  "f_name": f_name.get(),
                  "l_name": l_name.get(),
                  "address": address.get(),
                  "city": city.get(),
                  "zipcode": zipcode.get()
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
    query_label.grid(row=11, column=0, columnspan=2)

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
delete_box_label = Label(window, text="Numer ID")
delete_box_label.grid(row=8, column=0, pady=5)

# Stworzenie przycisków zatwierdzania
submit_button = Button(window, text="Dodaj rekord do bazy danych", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Stworzenie przycisku przeszukania bazy danych
query_btn = Button(window, text="Pokaż rekordy", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

# Stworzenie przycisku do usuwania
delete_btn = Button(window, text="Usuń rekord", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

# Stworzenie przycisku do edycji danych
edit_btn = Button(window, text="Edytuj rekord", command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

# Zatwierdzenie zmian
conn.commit()

# Zamykanie połączenia z bazą danych
conn.close()

window.mainloop()