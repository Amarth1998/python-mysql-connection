#insert data in table (deatils)
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@',database='HELLO')
print("succesfull connected")
cur=db.cursor()

s='insert into deatils values(01,"amarth",96.54)'
cur.execute(s) 

db.commit() #commit is used to save and  reflect  changes  in databases 