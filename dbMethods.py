import sqlite3
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

def addSpecies(conn, added):
    """Add a new species to the database.

    Args:
        conn (Connection): The database connection object.
        added (tuple): A tuple containing species data (species, morph, scientific_name, image).
    """
    try:
        cursor = conn.cursor()
        sql = '''INSERT INTO species(species, morph, scientific_name, image)
                 VALUES(?, ?, ?, ?)'''
        cursor.execute(sql, added)
        conn.commit()
        print("Species added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding species: {e}")

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