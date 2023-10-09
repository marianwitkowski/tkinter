
# bazowe okno aplikacji
import tkinter as tk
from tkinter import messagebox

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Widgrty w aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
root.geometry(f"{screen_width//2}x{screen_height//2}")
root.minsize(300, 350) # min. wielk. 300x350

def open_new_window():
    # tworzenie nowego okna
    new_window = tk.Toplevel(root)
    new_window.title("Nowe okno")
    tk.Label(new_window, text="To jest nowe okno").pack(padx=20, pady=20)

def close_application():
    answer = messagebox.askyesno("Zamknięcie aplikacji", "Czy na pewno?")
    if answer:
        root.destroy()

def on_button_click(button):
    print(f"Naciśnięto przycisk {button}")
    for key in button.keys():
        print(f"{key} - {button[key]}")

button_new_window = tk.Button(root, text="Otwórz nowe okno", command=open_new_window)
button_new_window.pack(pady=10)

button_close_window = tk.Button(root, text="Zamknij aplikację", command=close_application)
button_close_window.pack(pady=10)

colored_button = tk.Button(root, text="Kolorowy przycisk", bg="lightblue", fg="red" )
colored_button.pack(pady=10)

font_button = tk.Button(root, text="Font przycisku", font=("Courier", 22, "bold") )
font_button.pack(pady=10)

border_button = tk.Button(root, text="Border przycisku", bd=5, relief="ridge" )
border_button.pack(pady=10)

photo = tk.PhotoImage(file="pg_logo.png")
image_button = tk.Button(root, image=photo, text="Przycisk z logo", compound="left",
                         command=lambda: on_button_click(image_button))
image_button.pack(pady=10)

root.mainloop()