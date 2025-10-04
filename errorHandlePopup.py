import tkinter as tk

class ErrorPopup:
    def __init__(self, message):
        self.window = tk.Toplevel()
        self.window.title("Error")
        self.window.geometry("400x200")


        self.label = tk.Label(self.window, text=message, bg="white", fg="black", font=("Arial", 12), wraplength=300)
        self.label.pack(pady=20)

        self.ok_button = tk.Button(self.window, text="OK", command=self.close, bg="white", fg="black", font=("Arial", 12))
        self.ok_button.pack(pady=10)

    def close(self):
        self.window.destroy()