
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

selected_var = tk.StringVar()

def show_selection():
    result = selected_var.get()
    label.config(text=result)

radiobutton1 = tk.Radiobutton(root, command=show_selection, text="Opcja 1", value="A", variable=selected_var, indicatoron=0, width=40)
radiobutton1.pack(pady=10)

radiobutton2 = tk.Radiobutton(root, command=show_selection, text="Opcja 2", value="B", variable=selected_var, indicatoron=0, width=40)
radiobutton2.pack(pady=10)

radiobutton3 = tk.Radiobutton(root, command=show_selection, text="Opcja 3", value="C", variable=selected_var, indicatoron=0, width=40)
radiobutton3.pack(pady=10)

# wyswietl zaznaczenie w label
label = tk.Label(root, text="------", font=("Arial", 18))
label.pack(pady=10)

root.mainloop()