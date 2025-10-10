import sqlite3
import data
import os
import PopupHandler

# dbMethods.py
# This module contains methods for database operations.



def create_connection(dbFile):
    """Create a database connection to the SQLite database specified by dbFile.

    Args:
        dbFile (string): The path to the database file.

    Returns:
        Connection: The database connection object or None if the connection failed.
    """
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print(f"Connection to {dbFile} established.")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def close_connection(conn):
    """Close the database connection.

    Args:
        conn (Connection): The database connection object to close.
    """
    if conn:
        conn.close()
        print("Connection closed.")

def addSpecies(species):
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    if conn:
        try:
            cursor = conn.cursor()

            # Check if species with same name and morph already exists
            cursor.execute("SELECT * FROM species WHERE species = ? AND morph = ?", (species[0], species[1]))
            if cursor.fetchone():
                PopupHandler.ErrorPopup("Species with the same name and morph already exists.")
                return

            sql = '''INSERT INTO species(species, morph, scientific_name, image)
                     VALUES(?, ?, ?, ?)'''
            cursor.execute(sql, species)
            conn.commit()
            PopupHandler.SuccessPopup("Species added successfully.")
        except sqlite3.Error as e:
            PopupHandler.ErrorPopup(f"Error adding species: {e}")
        finally:
            close_connection(conn)

def getSpecies():
    """Retrieve all species from the database.

    Returns:
        list: A list of tuples containing species names.
    """
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    species_names = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM species")
            species_names = cursor.fetchall()
            print("Species retrieved successfully.")
        except sqlite3.Error as e:
            print(f"Error retrieving species: {e}")
        finally:
            close_connection(conn)
    return species_names

def deleteSpecies(species, morph):
    """Delete a species from the database.

    Args:
        species (str): The name of the species to delete.
        morph (str): The morph of the species to delete.
    """
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    if conn:
        try:
            cursor = conn.cursor()
            sql = '''DELETE FROM species WHERE species = ? AND morph = ?'''
            cursor.execute(sql, (species, morph))
            conn.commit()
            print("Species deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting species: {e}")
        finally:
            close_connection(conn)

def addBug(added):
    """Add a new bug to the database.

    Args:
        added (tuple): A tuple containing bug data (date_found, species, morph, source, humidity, temperature).
    """

    for i in range(len(added)):
        if added[i] == "":
            PopupHandler.ErrorPopup("All fields must be filled out.")
            return

    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    if conn:
        try:
            cursor = conn.cursor()
            sql = '''INSERT INTO bugs(nickname, date_found, species, morph, source, humidity, temperature, seen_owned)
                     VALUES(?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(sql, added)
            conn.commit()
            print("Bug added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding bug: {e}")
        finally:
            close_connection(conn)

def getBugs():
    """Retrieve all bugs from the database.

    Returns:
        list: A list of tuples containing bug data.
    """
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    bugs = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bugs")
            bugs = cursor.fetchall()
            print("Bugs retrieved successfully.")
        except sqlite3.Error as e:
            print(f"Error retrieving bugs: {e}")
        finally:
            close_connection(conn)
    return bugs

def getBugByNickname(nickname):
    """Retrieve a bug by its nickname.

    Args:
        nickname (str): The nickname of the bug to retrieve.

    Returns:
        tuple: A tuple containing the bug data.
    """
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    bug = None
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bugs WHERE nickname = ?", (nickname,))
            bug = cursor.fetchone()
        except sqlite3.Error as e:
            PopupHandler.ErrorPopup(f"Error retrieving bug: {e}")
        finally:
            close_connection(conn)
    return bug

def deleteBug(nickname):
    """Delete a bug from the database.

    Args:
        nickname (str): The nickname of the bug to delete.
    """
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    if conn:
        try:
            cursor = conn.cursor()
            sql = '''DELETE FROM bugs WHERE nickname = ?'''
            cursor.execute(sql, (nickname,))
            conn.commit()
            print("Bug deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting bug: {e}")
        finally:
            close_connection(conn)

def create_tables(conn):
    """Create necessary tables in the database.

    Args:
        conn (Connection): The database connection object.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        sqlTables = [
            """CREATE TABLE species (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                species TEXT NOT NULL,
                morph TEXT,
                scientific_name TEXT NOT NULL,
                image BLOB NOT NULL
            );""",
            """CREATE TABLE bugs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nickname TEXT NOT NULL,
                date_found DATE NOT NULL,
                species TEXT NOT NULL,
                morph TEXT,
                source TEXT NOT NULL,
                humidity TEXT NOT NULL,
                temperature TEXT NOT NULL,
                seen_owned INTEGER NOT NULL
                image BLOB
            );""",
            """CREATE TABLE notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bug_id INTEGER,
                note TEXT NOT NULL,
                date_added DATE NOT NULL,
                FOREIGN KEY (bug_id) REFERENCES bugs (id) 
            );"""
        ]
        for sql in sqlTables:
            cursor.execute(sql)
        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def convertImageBlob(image_path):
    """Convert image to blob for storing in database

    Args:
        image_path (str): the path to an image file

    Returns:
        anomalousBlob (bytes): img data become bytes
    """
    if not os.path.exists(image_path): 
        return None
    return (open(image_path, 'rb').read()) 

def convertBlobImage(blob, output_path):
    """Convert blob to image for retrieving from database

    Args:
        blob (bytes): the image data in bytes
        output_path (str): the path to save the image file

    Returns:
        None
    """
    try:
        open(output_path, 'wb').write(blob)
    
    except Exception as e:
        print(f"Error writing blob to file: {e}")