#INSATLL module mysql-connector-python
#type on command propmt = pip install mysql-connector-python
#than import mysql.connector for making a connection between mysql and python

import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@')
print("succesfull connected")

#create a database using python 
cur=db.cursor()

#NOW YOU CAN RUN SQL COMMAND USING PYTHON 
cur.execute('CREATE DATABASE HELLO') #A HELLO SCHEMA IS CREATED IN DATABASE.
