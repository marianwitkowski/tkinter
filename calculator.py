
# Kalkulator w TKinter
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator")
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.create_controls()
    def create_controls(self):
        self.display = tk.Entry(self.master, textvariable=self.result_var, font=("Arial", 24),
                                bd=10, state=tk.DISABLED)
        self.display.grid(row=0, column=0, columnspan=4)
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]
        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.master, text=button,
                      command= lambda b = button: self.on_button_click(b),
                      padx=20, pady=20, font=("Arial",20)).grid(row=row, column=col)
            col += 1 # col = col + 1
            if col>3:
                col = 0
                row += 1 # row = row + 1

    def on_button_click(self, char):
        pass

# main program
root = tk.Tk()
calc = Calculator(root)
root.mainloop()