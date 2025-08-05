import sqlite3
import data
import os
# dbMethods.py
# This module contains methods for database operations.


def printBugs():
    """Print all bugs in the database.
    """
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bugs")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Error retrieving bugs: {e}")
        finally:
            close_connection(conn)

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
            sql = '''INSERT INTO species(species, morph, scientific_name, image)
                     VALUES(?, ?, ?, ?)'''
            cursor.execute(sql, species)
            conn.commit()
            print("Species added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding species: {e}")
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
            cursor.execute("SELECT species FROM species")
            species_names = cursor.fetchall()
            print("Species retrieved successfully.")
        except sqlite3.Error as e:
            print(f"Error retrieving species: {e}")
        finally:
            close_connection(conn)
    return species_names

def addBug(added):
    """Add a new bug to the database.

    Args:
        added (tuple): A tuple containing bug data (date_found, species_name, source, humidity, temperature).
    """
    conn = create_connection(data.UserLocalAppdata.DBFILE.value)
    if conn:
        try:
            cursor = conn.cursor()
            sql = '''INSERT INTO bugs(nickname, date_found, species_name, source, humidity, temperature)
                     VALUES(?, ?, ?, ?, ?, ?)'''
            cursor.execute(sql, added)
            conn.commit()
            print("Bug added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding bug: {e}")
        finally:
            close_connection(conn)

def create_tables(conn):
    """Create necessary tables in the database.

    Args:
        conn (Connection): The database connection object.
    """
    try:
        cursor = conn.cursor()
        sqlTables = [
            """CREATE TABLE IF NOT EXISTS species (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                species TEXT NOT NULL,
                morph TEXT,
                scientific_name TEXT NOT NULL,
                image BLOB NOT NULL
            );""",

            """CREATE TABLE IF NOT EXISTS bugs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nickname TEXT NOT NULL,
                date_found DATE NOT NULL,
                species_name TEXT,
                source TEXT NOT NULL,
                humidity TEXT NOT NULL,
                temperature TEXT NOT NULL,
                FOREIGN KEY (species_name) REFERENCES species (species)
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
        raise FileNotFoundError(f"Image file {image_path} does not exist. :[")
    
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