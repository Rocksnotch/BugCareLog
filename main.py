import data
import dbMethods as db
import os

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
    

    conn = db.create_connection(data.UserLocalAppdata.DBFILE.value)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM species")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close_connection(conn)