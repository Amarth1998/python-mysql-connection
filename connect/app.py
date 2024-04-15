from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['fname']
    lname = request.form['lname']

    conn = sqlite3.connect('student.db')
    c = conn.cursor()

    c.execute('INSERT INTO classa (name, surname) VALUES (?, ?)', (name, lname))
    conn.commit()
    conn.close()

    return 'Data inserted successfully'


