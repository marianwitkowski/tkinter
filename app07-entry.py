
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

def show_entry():
    #result = entry.get()
    result = memo.get("1.0", tk.END)
    label.config(text=result)

entry = tk.Entry(root, font=("Arial", 22), justify="center")
entry.pack(pady=10)

memo = tk.Text(root, height=5, width=40, wrap="word")
memo.pack(pady=10)

button = tk.Button(root, text="Pokaż treść", command=show_entry)
button.pack()

# wyswietl zaznaczenie w label
label = tk.Label(root, text="------", font=("Arial", 18))
label.pack(pady=10)

root.mainloop()