#taking input from user and stroing data in database
#inserting multiple records

import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@',database='HELLO')
cur=db.cursor()

roll=int(input("Enter your roll number \n"))
name=input("Enter your name\n")
mark=int(input("Enter your marks \n")) 
s='insert into deatils values(%s,%s,%s)'
t=(roll,name,mark)  #this  is list of tuple
cur.execute(s,t)

db.commit() #commit is used to save and  reflect  changes  in databases 
print("succesfull ")