import sqlite3
import os


def create_note(text):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    connection.execute(
        "INSERT INTO Note (TEXT) VALUES (?);", (text,))
    connection.commit()

def read_notes():
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    notes = cur.execute("SELECT * FROM NOTE;").fetchall()
    connection.close()
    return notes

def read_note_by_id(id):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    product= cur.execute("SELECT * FROM NOTE WHERE ID=?;", (id,)).fetchone()
    connection.close()
    return product

def update_note(note_id, text):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    connection.execute(
        "UPDATE NOTE SET TEXT=?, WHERE NOTE_ID=?;", (text,id,))
    connection.commit()


def delete_note(note_id):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    connection.execute(
        "DELETE FROM NOTE WHERE NOTE_ID=?;",(note_id,))
    connection.commit()
