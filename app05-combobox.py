
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

def on_combobox_selected(event):
    result = combobox.get()
    label.config(text=result)

combobox = ttk.Combobox(root, values=["Opcja 1","Opcja 2","Opcja3"], state="readonly")
combobox.bind("<<ComboboxSelected>>", on_combobox_selected)
combobox.set("Opcja 3")
combobox.config(state="disabled")
combobox.pack(pady=20)

# wyswietl zaznaczenie w label
label = tk.Label(root, text="------", font=("Arial", 18))
label.pack(pady=10)

root.mainloop()