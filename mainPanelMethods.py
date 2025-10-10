import tkinter as tk
from tkinter.filedialog import askopenfilename
import data
import dbMethods as db
from tkcalendar import DateEntry
import PopupHandler

def browseImage(entry):
    """Open a file dialog to select an image and update the entry with the selected file path.

    Args:
        entry (tk.Entry): The tkinter entry widget to update with the selected file path.
    """
    filename = askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;"), ("All Files", "*.*")]
    )
    if filename:
        entry.config(state='normal')  # Enable the entry to update its content
        entry.delete(0, tk.END)  # Clear current content
        entry.insert(0, filename)  # Insert the selected file path
        entry.config(state='disabled')  # Disable the entry again to prevent user editing

def handleSpeciesDeletion(frame, tree):
    """Handle the deletion of a species from the database.

    Args:
        frame (tk.Frame): The tkinter frame to display the main panel.
        tree (tk.ttk.Treeview): The treeview widget containing the species list.
    """

    selected_item = tree.selection()
    if not selected_item:
        PopupHandler.ErrorPopup("Error: No species selected. Please select a species to delete.")
        return
    species_name = tree.item(selected_item)['values'][0]
    morph = tree.item(selected_item)['values'][1]
    try:
        PopupHandler.YesNoPopup(
            f"Are you sure you want to delete the species '{species_name}' with morph '{morph}'? This action cannot be undone.",
            yes_callback=lambda: [db.deleteSpecies(species_name, morph), mainSpeciesDB(frame), PopupHandler.SuccessPopup(f"Species '{species_name}' with morph '{morph}' deleted successfully.")],
            no_callback=lambda: None
        )
    except Exception as e:
        PopupHandler.ErrorPopup(f"Error: {str(e)}")

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

    # Nickname Label and Entry
    nicknameLabel = tk.Label(frame, text="Nickname:", bg=data.Colors.MAIN.value , fg="black", font=("Arial", 12))
    

    nicknameEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    nicknameEntry.config(relief=tk.SUNKEN, bd=2, width=50)

    # Date Acquired Label and Entry
    dateAcquiredLabel = tk.Label(frame, text="Date Acquired:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    dateAcquiredEntry = DateEntry(frame, bg="white", fg="black", font=("Arial", 12), date_pattern='yyyy-mm-dd')

    # Species Label and drop down selection list
    speciesLabel = tk.Label(frame, text="Species:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))

    speciesEntry = tk.StringVar(frame)
    speciesEntry.set("Select Species")
    try:
        speciesDropdown = tk.OptionMenu(frame, speciesEntry, *[f"{specie[1]} ({specie[2]})" for specie in db.getSpecies()])
        speciesDropdown.config(bg="white", fg="black", font=("Arial", 12))
    except:
        PopupHandler.ErrorPopup("Error: Could not retrieve species from database. Please ensure the database is set up correctly and contains species data.")
        return
    # Source Label and Entry
    sourceLabel = tk.Label(frame, text="Source:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))

    sourceEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    sourceEntry.config(relief=tk.SUNKEN, bd=2, width=50)

    # Humidity Label and Entry
    humidityLabel = tk.Label(frame, text="Humidity:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))

    humidityEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    humidityEntry.config(relief=tk.SUNKEN, bd=2, width=50)

    # Temperature Label and Entry
    temperatureLabel = tk.Label(frame, text="Temperature:", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))

    temperatureEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    temperatureEntry.config(relief=tk.SUNKEN, bd=2, width=50)

    # Radio buttons to select either Seen or Owned, default to Seen
    seenOwnedChoice = tk.IntVar()
    seenRadioButton = tk.Radiobutton(frame, text="Seen", variable=seenOwnedChoice, value=0, bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    ownedRadioButton = tk.Radiobutton(frame, text="Owned", variable=seenOwnedChoice, value=1, bg=data.Colors.MAIN.value, fg="black", font=("Arial", 12))
    seenRadioButton.select()

    speciesEntry.trace_add("write", lambda *args: speciesEntry.set(speciesEntry.get()))
    # Add Bug Button, uses method from dbMethods to add the bug
    addBugButton = tk.Button(frame, text="Add Bug", command=lambda: db.addBug(
        ( 
            nicknameEntry.get(),
            dateAcquiredEntry.get(),
            speciesEntry.get(),
            sourceEntry.get(),
            humidityEntry.get(),
            temperatureEntry.get(),
            seenOwnedChoice.get()
        )
    ))
    addBugButton.config(bg=data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, width=20, height=2)
    
    # Place all here
    addBugLabel.place(relx=0.03, rely=0.05)
    nicknameLabel.place(relx=0.03, rely=0.1)
    nicknameEntry.place(relx=0.035, rely=0.13, width=500, height=30)
    dateAcquiredLabel.place(relx=0.03, rely=0.18)
    dateAcquiredEntry.place(relx=0.035, rely=0.21, width=200, height=30)
    speciesLabel.place(relx=0.03, rely=0.26)
    speciesDropdown.place(relx=0.035, rely=0.29, width=500, height=30)
    sourceLabel.place(relx=0.03, rely=0.34)
    sourceEntry.place(relx=0.035, rely=0.37, width=500, height=30)
    humidityLabel.place(relx=0.03, rely=0.42)
    humidityEntry.place(relx=0.035, rely=0.45, width=500, height=30)
    temperatureLabel.place(relx=0.03, rely=0.5)
    temperatureEntry.place(relx=0.035, rely=0.53, width=500, height=30)
    seenRadioButton.place(relx=0.03, rely=0.57)
    ownedRadioButton.place(relx=0.15, rely=0.57)
    addBugButton.place(relx=0.03, rely=0.63)

def mainViewBugs(frame):
    """Display the list of bugs in the database.

    Args:
        frame (tk.Frame): The tkinter frame to display the main panel.
    """
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    # Top Label
    viewBugsLabel = tk.Label(frame, text="View Bugs", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 16, 'bold'))
    viewBugsLabel.place(relx=0.03, rely=0.05)

    viewBugsTree = tk.ttk.Treeview(frame, columns=("Nickname", "Date Found", "Species", "Seen/Owned"), show='headings')
    viewBugsTree.heading("Nickname", text="Nickname")
    viewBugsTree.column("Nickname", width=150)
    viewBugsTree.heading("Date Found", text="Date Found")
    viewBugsTree.column("Date Found", width=75)
    viewBugsTree.heading("Species", text="Species")
    viewBugsTree.column("Species", width=150)
    viewBugsTree.heading("Seen/Owned", text="Seen/Owned")
    viewBugsTree.column("Seen/Owned", width=75)

    bugs = db.getBugs()
    for bug in bugs:
        print(bug)
        if bug[7] == 0:
            bugSeenOwned = "Seen"
        else:
            bugSeenOwned = "Owned"

        viewBugsTree.insert("", "end", values=(bug[1], bug[2], bug[3], bugSeenOwned))

    viewBugsTree.place(relx=0.035, rely=0.1, width=500, height=400)

def mainSpeciesDB(frame):
    """Handle Species DB operation.

    Args:
        frame (tk.Frame): The tkinter frame to display the main panel.
    """

    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Top Label
    speciesDBLabel = tk.Label(frame, text="Species Database", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 16, 'bold'))

    # Species Treeview
    viewSpeciesTree = tk.ttk.Treeview(frame, columns=("Species", "Morph", "Scientific Name"), show='headings')
    viewSpeciesTree.heading("Species", text="Species")
    viewSpeciesTree.column("Species", width=150)
    viewSpeciesTree.heading("Morph", text="Morph")
    viewSpeciesTree.column("Morph", width=150)
    viewSpeciesTree.heading("Scientific Name", text="Scientific Name")
    viewSpeciesTree.column("Scientific Name", width=150)

    # Populate the treeview with species data from the database
    species = db.getSpecies()
    for specie in species:
        viewSpeciesTree.insert("", "end", values=(specie[1], specie[2], specie[3]))

    # Add Species Button
    addSpeciesButton = tk.Button(frame, text="Add Species", command=lambda: addSpecies(frame))
    addSpeciesButton.config(bg=data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, width=20, height=2)

    deleteSpeciesButton = tk.Button(frame, text="Delete Species", command=lambda: handleSpeciesDeletion(frame, viewSpeciesTree))
    deleteSpeciesButton.config(bg=data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, width=20, height=2)
    

    viewSpeciesTree.place(relx=0.035, rely=0.1, width=500, height=400)
    deleteSpeciesButton.place(relx=0.56, rely=0.6)
    addSpeciesButton.place(relx=0.03, rely=0.6)
    speciesDBLabel.place(relx=0.03, rely=0.05)

def addSpecies(frame):
    """Handle Add Species operation.

    Args:
        frame (tk.Frame): The tkinter frame to display the main panel.
    """

    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Top Label
    addSpeciesLabel = tk.Label(frame, text="Add New Species", bg=data.Colors.MAIN.value, fg="black", font=("Arial", 16, 'bold'))
    

    # Species Label and Entry
    speciesLabel = tk.Label(frame, text="Species:", bg=data.Colors.MAIN.value , fg="black", font=("Arial", 12))

    speciesEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    speciesEntry.config(relief=tk.SUNKEN, bd=2, width=50)

    # Morph Label and Entry
    morphLabel = tk.Label(frame, text="Morph:", bg=data.Colors.MAIN.value , fg="black", font=("Arial", 12))
    

    morphEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    morphEntry.config(relief=tk.SUNKEN, bd=2, width=50)
    

    # Scientific Name Label and Entry
    scientificNameLabel = tk.Label(frame, text="Scientific Name:", bg=data.Colors.MAIN.value , fg="black", font=("Arial", 12))
    

    scientificNameEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    scientificNameEntry.config(relief=tk.SUNKEN, bd=2, width=50)
    

    # Image Label and Small Open File Button
    imageLabel = tk.Label(frame, text="Thumbnail Image (200x100):", bg=data.Colors.MAIN.value , fg="black", font=("Arial", 12))

    imageButton = tk.Button(frame, text="Browse", command=lambda: browseImage(imageLocationEntry))
    imageButton.config(bg=data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2)

    imageLocationEntry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    imageLocationEntry.config(relief=tk.SUNKEN, bd=2, width=50, state='disabled')

    # Add Species Button
    addSpeciesButton = tk.Button(frame, text="Add Species", command=lambda: db.addSpecies((
        speciesEntry.get(),
        morphEntry.get(),
        scientificNameEntry.get(),
        db.convertImageBlob(imageLocationEntry.get())
    )))
    addSpeciesButton.config(bg=data.Colors.NAVBUTTONS.value, fg="black", font=("Arial", 12), relief=tk.RAISED, bd=2, width=20, height=2)
    

    #All places here
    addSpeciesButton.place(relx=0.03, rely=0.5)
    addSpeciesLabel.place(relx=0.03, rely=0.05)
    imageButton.place(relx=0.035, rely=0.37, width=500, height=30)
    scientificNameEntry.place(relx=0.035, rely=0.29, width=500, height=30)
    imageLabel.place(relx=0.03, rely=0.34)
    morphEntry.place(relx=0.035, rely=0.21, width=500, height=30)
    morphLabel.place(relx=0.03, rely=0.18)
    scientificNameLabel.place(relx=0.03, rely=0.26)
    speciesEntry.place(relx=0.035, rely=0.13, width=500, height=30)
    speciesLabel.place(relx=0.03, rely=0.1)
    addSpeciesLabel.place(relx=0.03, rely=0.05)
    imageLocationEntry.place(relx=0.035, rely=0.42, width=400, height=30)