
# bazowe okno aplikacji
import tkinter as tk
from tkinter import ttk
import requests

root = tk.Tk() # tworzenie glownego okna aplikacji
root.title("Widgrty w aplikacji") # ustawienie tytulu okna

#root.geometry("800x600+100+150") # wielk. 800x600 i przesuniecie 100 od lewej i 150 o gory
screen_width = root.winfo_screenwidth() # pobranie szer. ekranu
screen_height = root.winfo_screenheight() # pobranie wys. ekranu
root.geometry(f"{screen_width//2}x{screen_height//2}")
root.minsize(300, 350) # min. wielk. 300x350

def get_weather():
    city_name = entry.get().strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?&units=metric&q={city_name}&APPID=df038b26e3d87a210eaf2ab991eb1485"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"niepoprawna odpowiedź z serwisu - {response.status_code}")
        weather_data = response.json()
        weather = weather_data.get("main")
        temperature = weather.get("temp")
        humidity = weather.get("humidity")
        temp_max = weather.get("temp_max")
        temp_min = weather.get("temp_min")
        pressure = weather.get("pressure")
        print(temperature, humidity, temp_min, temp_max, pressure)
        labels_list[0].configure(text=f"Temp.: {temperature}st.C.")
        labels_list[1].configure(text=f"Wilgotność: {humidity}%")
        labels_list[2].configure(text=f"Temp min.: {temp_min}st.C")
        labels_list[3].configure(text=f"Temp max.: {temp_max}st.C")
        labels_list[4].configure(text=f"Ciśnienie: {pressure}hPa")
    except Exception as exc:
        labels_list[0].configure(text=f"ERROR: {exc}")

entry = tk.Entry(root, font=("Arial", 22), justify="center", width=20)
entry.place(x= 20, y= 30)

button = tk.Button(root, text="Pokaż pogodę", command=get_weather )
button.place(x= 350, y=30)

labels_list = []
y = 100
for i in range(5):
    label = tk.Label(root, text="-------")
    labels_list.append(label)
    label.place(x=50, y=y)
    y += 50




root.mainloop()