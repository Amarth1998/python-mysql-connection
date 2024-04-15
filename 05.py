#inserting multiple records

import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@',database='HELLO')
print("succesfull connected")
cur=db.cursor()
s='insert into deatils values(%s,%s,%s)'
t=[(2,"patel",25.2),(41,"dd",45.2),(12,"ss",10.10)]  #this  is list of tuple
cur.executemany(s,t)  #executemany() method to store many data in once

db.commit() #commit is used to save and  reflect  changes  in databases 
print("succesfull ")