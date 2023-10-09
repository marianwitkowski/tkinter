
# bazowe okno aplikacji
import tkinter as tk

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Widgrty w aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
root.geometry(f"{screen_width//2}x{screen_height//2}")
root.minsize(300, 350) # min. wielk. 300x350

# funkcja obsluguja nacisniecie przycisku
def change_text_label():
    print("button click")
    # modyfikacja tekst obiektu typu Label
    label.config(text="Nowy tekst na obiekcie label")


# wstawianie kontrolek
# tworzenie etykiety tekstowej
label = tk.Label(root, text="Etykieta testowa", justify="left", font=("Arial", 30) )
label.pack(pady=20)

# tworzenie przycisku
button = tk.Button(root, text="Ustaw tekst etykiety", command=change_text_label)
button.pack(pady=20)

root.mainloop()