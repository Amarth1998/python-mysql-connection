import mysql.connector
import cgi
print("<h1>welcome to python</h1>")
form = cgi.FieldStorage()
name = form.getvalue("firstname")
surname = form.getvalue("lastname")

db=mysql.connector.connect(host='localhost',user='root', password="1234",database='student')
cur=db.cursor()


a="INSERT INTO classa VALUES (%s,%s)"
b=(name,surname)
cur.execute(a,b)

db.commit()

# Print a success message
print("Content-type: text/html")
print()
print("<h1>Message sent!</h1>")
