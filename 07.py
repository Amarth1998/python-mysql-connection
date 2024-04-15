# fetching data from database
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root', password='qwertyuiopasdfghjklzxcvbnm1998@',database='HELLO')
cur=db.cursor()

s='select * from deatils'

cur.execute(s)

#use can also use fetchone to fetch only one data  
p=cur.fetchall()
print(p)

  output:[(1, 'amarth', 96.54), (2, 'patel', 25.2), (2, 'patel', 25.2), (41, 'dd', 45.2), (12, 'ss', 10.1), (48, 'hello', 789.0)]

for i in p:
    print(i)
output:
(1, 'amarth', 96.54)
(2, 'patel', 25.2)
(2, 'patel', 25.2)
(41, 'dd', 45.2)
(12, 'ss', 10.1)
(48, 'hello', 789.0)    

for i in p:
    for j in i:
        print(j,end=" ")
    print()   
output:
1 amarth 96.54 
2 patel 25.2
2 patel 25.2
41 dd 45.2
12 ss 10.1
48 hello 789.0     

