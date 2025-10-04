import tkinter as tk
import data
import mainPanelMethods as mainPanel


def navGeneral(frame, mainFrame):
    """Handle general navigation actions.

    Args:
        frame (tk.Frame): The tkinter frame to navigate.
    """

    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Nav Frame Label, place to the left of parent
    navLabel = tk.Label(frame, text="Navigation", bg=data.Colors.NAVIGATION.value, fg="black", font=("Arial", 16))
    navLabel.place(relx=0.03, rely=0.05)

    # Buttons for main navigation
    speciesDB = tk.Button(frame, text="Species DB", command=lambda: mainPanel.mainSpeciesDB(mainFrame))
    speciesDB.config(bg = data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, anchor = "w", width=20, height=2)
    speciesDB.place(relx=0.035, rely=0.1)

    addBug = tk.Button(frame, text="Add Bug", command=lambda: mainPanel.mainAddBug(mainFrame))
    addBug.config(bg = data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, anchor = "w", width=20, height=2)
    addBug.place(relx=0.035, rely=0.17)

    bugList = tk.Button(frame, text="Bug List", command=lambda: mainPanel.mainViewBugs(mainFrame))
    bugList.config(bg = data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, anchor = "w", width=20, height=2)
    bugList.place(relx=0.035, rely=0.24)

    careLogs = tk.Button(frame, text="Care Logs", command=lambda: print("Care Logs Clicked"))
    careLogs.config(bg = data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, anchor = "w", width=20, height=2)
    careLogs.place(relx=0.035, rely=0.31)

    moltHistory = tk.Button(frame, text="Molt History", command=lambda: print("Molt History Clicked"))
    moltHistory.config(bg = data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, anchor = "w", width=20, height=2)
    moltHistory.place(relx=0.035, rely=0.38)

    notes = tk.Button(frame, text="Notes", command=lambda: print("Notes Clicked"))
    notes.config(bg = data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, anchor = "w", width=20, height=2)
    notes.place(relx=0.035, rely=0.45)

    reminders = tk.Button(frame, text="Reminders", command=lambda: print("Reminders Clicked"))
    reminders.config(bg = data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, anchor = "w", width=20, height=2)
    reminders.place(relx=0.035, rely=0.52)
