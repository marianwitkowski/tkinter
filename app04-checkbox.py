
# bazowe okno aplikacji
import tkinter as tk

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Widgrty w aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
root.geometry(f"{screen_width//2}x{screen_height//2}")
root.minsize(300, 350) # min. wielk. 300x350

# deklaracja zmiennych przechowujacych stan checkbox'ow
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

def show_selection():
    selections = []
    if var1.get():
        selections.append("Opcja 1")
    if var2.get():
        selections.append("Opcja 2")
    if var3.get():
        selections.append("Opcja 3")
    label.config( text=" - ".join(selections) )

checkbox1 = tk.Checkbutton(root, text="Opcja 1", font=("Arial", 25), variable=var1,
                           command=show_selection)
checkbox1.pack(pady=10)

checkbox2 = tk.Checkbutton(root, text="Opcja 2", font=("Arial", 25), variable=var2,
                           command=show_selection, fg="green")
checkbox2.pack(pady=10)

checkbox3 = tk.Checkbutton(root, text="Opcja 3", font=("Arial", 25), variable=var3,
                           command=show_selection)
checkbox3.pack(pady=10)

# wyswietl zaznaczenie w label
label = tk.Label(root, text="Zaznaczone opcje: BRAK", font=("Arial", 18))
label.pack(pady=10)

root.mainloop()