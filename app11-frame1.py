
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

# ramka górna
top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x", side="top")

# ramka dolna
bottom_frame = tk.Frame(root, bg="lightgreen", height=100)
bottom_frame.pack(fill="x", side="bottom")

# ramkal lewa
left_frame = tk.Frame(root, bg="red", width=400 )
left_frame.pack(side="left", fill="both", expand=True)

# ramkal prawa
right_frame = tk.Frame(root, bg="green", width=400 )
right_frame.pack(side="right", fill="both", expand=True)

root.mainloop()