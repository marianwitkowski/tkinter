
# bazowe okno aplikacji
import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Widgrty w aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
root.geometry(f"800x600")
root.minsize(300, 350) # min. wielk. 300x350

def open_modal_window(data_var):

    def close_modal():
        data_var.set( entry.get() )
        modal_window.destroy()

    modal_window = tk.Toplevel(root)
    modal_window.title("okno modalne")
    entry = tk.Entry(modal_window)
    entry.pack(padx=10, pady=10)

    close_button = tk.Button(modal_window, text="Zamknij", command=close_modal)
    close_button.pack(padx=10, pady=10)

    modal_window.grab_set() # ustaw okno jako modalne
    root.wait_window(modal_window)


data_from_modal = tk.StringVar()
open_button = tk.Button(root, text="Otwórz okno modalne", command=lambda: open_modal_window(data_from_modal) )
open_button.pack(pady=20)

label = tk.Label(root, textvariable=data_from_modal)
label.pack(pady=20)

root.mainloop()