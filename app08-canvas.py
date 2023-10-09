
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

canvas = tk.Canvas(root, width=400, height=400, bg="red")
canvas.pack(pady=10)

canvas.create_rectangle(10, 10, 100, 100, fill="blue", outline="white")

points = [210, 10, 150, 90, 250, 90]
canvas.create_polygon(points, fill="yellow", outline="black")

canvas.create_line(210, 110, 300, 200, fill="black", width=5)
canvas.create_line(210, 310, 300, 400, fill="blue", width=3, dash=(3,3))

root.mainloop()