import tkinter as tk
import data

class ErrorPopup:
    def __init__(self, message):
        self.window = tk.Toplevel()
        self.window.title("Error")
        self.window.geometry("400x200")


        self.label = tk.Label(self.window, text=message, bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12), wraplength=300)
        self.label.pack(pady=20)

        self.ok_button = tk.Button(self.window, text="OK", command=self.close, bg="white", fg="black", font=("Arial", 12))
        self.ok_button.pack(pady=10)

    def close(self):
        self.window.destroy()

class YesNoPopup:
    def __init__(self, message, yes_callback, no_callback):
        self.window = tk.Toplevel()
        self.window.title("Confirm")
        self.window.geometry("400x200")

        self.label = tk.Label(self.window, text=message, bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12), wraplength=300)
        self.label.pack(pady=20)

        self.yes_button = tk.Button(self.window, text="Yes", command=lambda: self.respond(yes_callback), bg="white", fg="black", font=("Arial", 12))
        self.yes_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.no_button = tk.Button(self.window, text="No", command=lambda: self.respond(no_callback), bg="white", fg="black", font=("Arial", 12))
        self.no_button.pack(side=tk.RIGHT, padx=20, pady=10)

    def respond(self, callback):
        callback()
        self.window.destroy()

class SuccessPopup:
    def __init__(self, message):
        self.window = tk.Toplevel()
        self.window.title("Success")
        self.window.geometry("400x200")

        self.label = tk.Label(self.window, text=message, bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12), wraplength=300)
        self.label.pack(pady=20)

        self.ok_button = tk.Button(self.window, text="OK", command=self.close, bg="white", fg="black", font=("Arial", 12))
        self.ok_button.pack(pady=10)

    def close(self):
        self.window.destroy()