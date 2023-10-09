
# bazowe okno aplikacji
import tkinter as tk
import os

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Tytuł aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
#root.geometry(f"{screen_width//2}x{screen_height//3}")
root.geometry(f"{int(screen_width/2)}x{int(screen_height/3)}")

# wariantowanie instrukcji na podstawie systemu operacyjnego
if os.name == "nt":
    root.iconbitmap("test.ico")
    #root.attributes("-disabled", True)
else:
    img = tk.PhotoImage(file="test.png")
    root.iconphoto(True, img)
    #root.attributes("-modified", True)

root.minsize(300, 350) # min. wielk. 300x350

root.mainloop()