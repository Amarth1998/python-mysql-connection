from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route('/submit', methods=['post'])
def submit():
    # Get the form data
    fname = request.form['fname']
    lname = request.form['lname']

    # Connect to the database
    conn = sqlite3.connect( host="localhost",
    user="root",
    password="1234",
    database="student")
    c = conn.cursor()

    # Insert the data into the database
    # sql = "INSERT INTO classa (name, surname) VALUES (%s, %s)"
    # values = (fname, lname)
    # c.execute(sql, values)
    c.execute('INSERT INTO classa (name, surname) VALUES (?, ?)', (fname, lname))
    conn.commit()

    # Close the database connection
    conn.close()

    # Return a response
    return 'Data inserted successfully!'


# import mysql.connector

# # Connect to the MySQL database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="student"
# )

# # Get the form data
# form = cgi.FieldStorage()
# fname = form.getvalue("fname")
# lname = form.getvalue("lname")

# # Insert the data into the database
# cursor = db.cursor()
# sql = "INSERT INTO classa (name, surname) VALUES (%s, %s)"
# values = (fname, lname)
# cursor.execute(sql, values)
# db.commit()

