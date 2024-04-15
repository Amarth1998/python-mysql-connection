# updating data from database
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@',database='HELLO')
cur=db.cursor()

s='UPDATE deatils SET MARKS=MARKS+2 WHERE ROLL_NUMBER=12'

cur.execute(s)
db.commit()
print("success")

  