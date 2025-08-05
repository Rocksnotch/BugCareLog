import data
import dbMethods as db
import os
import tkinter as tk
import navPanelMethods as nav
import mainPanelMethods as mainPanel

if __name__ == '__main__':

    # Check if the database folder exists, if not create it
    if not os.path.exists(data.UserLocalAppdata.DBFILE.value):
        os.makedirs(os.path.dirname(data.UserLocalAppdata.DBFILE.value), exist_ok=True)
        # Create a database connection
        connection = db.create_connection(data.UserLocalAppdata.DBFILE.value)

        # Create the necessary tables
        db.create_tables(connection)

        # Close the database connection
        db.close_connection(connection)

    test_image_path = "image.png"
    test_output_path = "output_image.png"

    # Convert image to blob
    #try:
        #blob = db.convertImageBlob(test_image_path)
        #print(f"Image converted to blob, {len(blob)} bytes.")
    #except Exception as e:
        #print(f"Error: {e}")

    # Convert blob back to image
    #try:
        #db.convertBlobImage(blob, test_output_path)
        #print(f"Blob written back to {test_output_path}.")
    #except Exception as e:
        #print(f"Error: {e}")  #(#there #has #to #be #an #easier #way)

# Initialize the main application window
root = tk.Tk()
root.title("My Bug Log")
root.config(bg="#D3D3D3")
root.geometry("800x800")  # Set a default size
#root.state('zoomed')

# Nav Frame
navFrame = tk.Frame(root, relief=tk.RAISED, bd = 2, bg=data.Colors.NAVIGATION.value, width=210)
navFrame.pack(side=tk.LEFT, fill=tk.BOTH)

# Main Frame
mainFrame = tk.Frame(root, bg=data.Colors.MAIN.value, width=590)
mainFrame.pack(side=tk.LEFT, fill=tk.BOTH)

# Initialize navigation panel
nav.navGeneral(navFrame, mainFrame) # Initialize navigation panel to default state

# Initialize main panel
mainPanel.mainPanelDefault(mainFrame)  # Initialize main panel to default state

# Start the main event loop
root.mainloop()