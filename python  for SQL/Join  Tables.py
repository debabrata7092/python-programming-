import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase1"
)

mycursor = mydb.cursor()



a="SELECT *FROM student INNER JOIN customers ON  student. id=customers. id";
 

mycursor.execute(a)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)