
# bazowe okno aplikacji
import tkinter as tk
from tkinter import ttk

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Widgrty w aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
root.geometry(f"{screen_width//2}x{screen_height//2}")
root.minsize(300, 350) # min. wielk. 300x350

def update_item():
    indices = listbox.curselection()
    if indices:
        ix = indices[0]
        # usun zaznaczony element
        listbox.delete(ix)
        # wstawic wiersz w miejsce wczesniej usunieto
        listbox.insert(ix, "Aktualizacja wiersza")

def on_listbox_select(event):
    # pobrac indeksy wszystkich wybranych elementow
    indices = listbox.curselection()
    if indices:
        selected_items = []
        for ix in indices:
            selected_items.append( listbox.get(ix) )
        label.config(text=",".join(selected_items))
    else:
        label.config(text="Brak zaznaczenia")

# deklaracja listboxa
listbox = tk.Listbox(root, fg="blue", bg="gray", selectbackground="yellow",
                     height=5, selectmode="multiple" )
listbox.pack(pady=20)
items = ["Element 1", "Element 2", "Element 3"]
for item in items:
    listbox.insert("end", item)
listbox.bind("<<ListboxSelect>>", on_listbox_select)

# wyswietl zaznaczenie w label
label = tk.Label(root, text="------", font=("Arial", 18))
label.pack(pady=10)

update_button = tk.Button(root, text="Aktualizuj zaznaczony wiersz", command=update_item)
update_button.pack(pady=10)

root.mainloop()