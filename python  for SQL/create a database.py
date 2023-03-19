import mysql.connector

mysqldb= mysql .connector.connect(
	host = "localhost",
	user = "root",
	password = ""
	)

db= mysqldb.cursor()
db.execute("CREATE DATABASE mydatabase1")