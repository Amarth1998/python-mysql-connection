#inserting multiple records

import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@',database='HELLO')
print("succesfull connected")
cur=db.cursor()
s='insert into deatils values(%s,%s,%s)'
t=(2,"patel",25.2)  #this is tuple
cur.execute(s,t) 

db.commit() #commit is used to save and  reflect  changes  in databases 