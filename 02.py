#create table
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@',database='HELLO')
print("succesfull connected")
cur=db.cursor()

cur.execute('CREATE TABLE deatils(roll_number int , student_name char(20) , marks float)') 
print("succesfull created table")
