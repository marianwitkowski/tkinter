
# bazowe okno aplikacji
import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Widgrty w aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
root.geometry(f"{screen_width//2}x{screen_height//2}")
root.minsize(300, 350) # min. wielk. 300x350

def item_selected(event):
    selected_items = table.selection()
    for i in selected_items:
        print(table.item(i)["values"])

subjects = ["Matematyka", "Fizyka", "PKM", "Geologia", "Materiałoznastwo"]
scores = ["2", "3", "4", "5"]

table = ttk.Treeview(root, columns=("przedmiot", "ocena"), show="headings" )
table.heading("przedmiot", text="Nazwa przedmiotu")
table.heading("ocena", text="Ocena z przedmiotu")
table.pack(fill="both", expand=True)
table.bind("<<TreeviewSelect>>", item_selected)

# dodać dane do treeview
for _ in range(100):
    subject = random.choice(subjects)
    score = random.choice(scores)
    table.insert(parent="", index=tk.END, values=(subject, score) )

root.mainloop()