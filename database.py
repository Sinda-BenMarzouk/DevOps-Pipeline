import sqlite3
import os

def create_db(database_filename):
    connection = sqlite3.connect(database_filename)
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS Note")
    cur.execute(
        "CREATE TABLE NOTE (ID INTEGER PRIMARY KEY, TEXT TEXT NOT NULL);")
    cur.execute(
        "INSERT INTO NOTE (TEXT) VALUES ('go shopping'),('go cinema'),('create project');")
    connection.commit()
    print("Done")
    connection.close()