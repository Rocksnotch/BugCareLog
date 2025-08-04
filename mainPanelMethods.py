import tkinter as tk
import data
import dbMethods as db
from tkcalendar import Calendar, DateEntry 

def mainPanelDefault(frame):
    """Handle default main panel display.

    Args:
        frame (tk.Frame): The tkinter frame to display the main panel.
    """

    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Top Label
    mainLabel = tk.Label(frame, text="Welcome to My Bug Log", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 16, 'bold'))
    mainLabel.place(relx=0.03, rely=0.05)

    # Description Label
    descriptionLabel = tk.Label(frame, text="Use the navigation panel to get started.", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    descriptionLabel.place(relx=0.03, rely=0.1)

def mainAddBug(frame):
    """Handle Add Bug operation.

    Args:
        frame (tk.Frame): The tkinter frame to display the main panel.
    """

    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Top Label
    addBugLabel = tk.Label(frame, text="Add New Bug", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 16, 'bold'))
    addBugLabel.place(relx=0.03, rely=0.05)

    # Nickname Label and Entry
    nicknameLabel = tk.Label(frame, text="Nickname:", bg=data.Colors.MAIN.value , fg="black", font=("Arial", 12))
    nicknameLabel.place(relx=0.03, rely=0.1)

    nicknameEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    nicknameEntry.config(relief=tk.SUNKEN, bd=2, width=50)
    nicknameEntry.place(relx=0.035, rely=0.13, width=500, height=30)

    # Date Acquired Label and Entry
    dateAcquiredLabel = tk.Label(frame, text="Date Acquired:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    dateAcquiredLabel.place(relx=0.03, rely=0.18)

    dateAcquiredEntry = DateEntry(frame, bg="white", fg="black", font=("Arial", 12), date_pattern='yyyy-mm-dd')
    dateAcquiredEntry.place(relx=0.035, rely=0.21, width=200, height=30)

    # Species Label and drop down selection list
    speciesLabel = tk.Label(frame, text="Species:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    speciesLabel.place(relx=0.03, rely=0.26)

    speciesEntry = tk.StringVar(frame)
    speciesEntry.set("Select Species")
    speciesDropdown = tk.OptionMenu(frame, speciesEntry, *db.getSpecies())
    speciesDropdown.config(bg="white", fg="black", font=("Arial", 12))
    speciesDropdown.place(relx=0.035, rely=0.29, width=500, height=30)

    # Source Label and Entry
    sourceLabel = tk.Label(frame, text="Source:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    sourceLabel.place(relx=0.03, rely=0.34)

    sourceEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    sourceEntry.config(relief=tk.SUNKEN, bd=2, width=50)
    sourceEntry.place(relx=0.035, rely=0.37, width=500, height=30)

    # Humidity Label and Entry
    humidityLabel = tk.Label(frame, text="Humidity:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    humidityLabel.place(relx=0.03, rely=0.42)

    humidityEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    humidityEntry.config(relief=tk.SUNKEN, bd=2, width=50)
    humidityEntry.place(relx=0.035, rely=0.45, width=500, height=30)

    # Temperature Label and Entry
    temperatureLabel = tk.Label(frame, text="Temperature:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    temperatureLabel.place(relx=0.03, rely=0.5)

    temperatureEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    temperatureEntry.config(relief=tk.SUNKEN, bd=2, width=50)
    temperatureEntry.place(relx=0.035, rely=0.53, width=500, height=30)

    # Add Bug Button, uses method from dbMethods to add the bug
    addBugButton = tk.Button(frame, text="Add Bug", command=lambda: db.addBug(
        (
            nicknameEntry.get(),
            dateAcquiredEntry.get(),
            speciesEntry.get(),
            sourceEntry.get(),
            humidityEntry.get(),
            temperatureEntry.get()
        )
    ))
    addBugButton.config(bg=data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, width=20, height=2)
    addBugButton.place(relx=0.035, rely=0.6)