import mysql .connector

medb= mysql.connector.connect(

host = "localhost",
user ="root",
password = "",
database ="mydatabase1"

)

mysql=medb.cursor()

mysql.execute("SELECT * FROM customers")

myresult =mysql.fetchall()

for x in myresult:
  print(x)