from cgitb import text
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from database import create_db
from note import create_note, update_note, read_note_by_id, delete_note

def create_app(name, test=False):
    if test:
        app = Flask(name,template_folder='../templates')
    else:
        app = Flask(name, template_folder='templates')

    # Index
    @app.route('/')
    def index():
        return render_template('index.html')


    # Create Note
    @app.route("/=", methods=['GET', 'POST'])
    def createnote():
        if request.method == 'POST':
            text= request.form['text']
            create_note(text)
            return redirect('/')
        else:
            return render_template('index.html')

    # Update Note
    @app.route('/update/<int:id>', methods=['GET', 'POST'])
    def updatenote(id):
        note = read_note_by_id(id)
        if request.method == 'POST':
            text = request.form['text']
            update_note(id,text)
            return redirect('/')
        else:
            return render_template('index.html')

    # Delete Note
    @app.route('/delete/<int:id>')
    def detelenote(id):
        note_to_delete = read_note_by_id(id)
        delete_note(note_to_delete[0])
        return redirect('/')


def main( db='todo.db', create=False):
    if create:
        create_db(db)
    os.environ['DATABASE_FILENAME'] = db
    app = create_app(__name__)
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()