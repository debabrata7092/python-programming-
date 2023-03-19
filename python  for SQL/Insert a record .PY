import mysql .connector

mydb=  mysql .connector.connect(

	host ="localhost",
	user ="root",
	password = "",
	database ="mydatabase1"

	)

db= mydb.cursor()

sql = "INSERT INTO customers (id,name, address) VALUES (%s, %s,%s)"
val = [
  ("",'Peter', 'Lowstreet 4'),
  ("",'Amy', 'Apple st 652'),
  ("",'Hannah', 'Mountain 21'),
  (4,'Michael', 'Valley 345'),
  ("",'Sandy', 'Ocean blvd 2'),
  (6,'Betty', 'Green Grass 1'),
  (7,'Richard', 'Sky st 331'),
  (8,'Susan', 'One way 98'),
  ("",'Vicky', 'Yellow Garden 2'),
  ("",'Ben', 'Park Lane 38'),
  ("",'William', 'Central st 954'),
  ("",'Chuck', 'Main Road 989'),
  ("",'Viola', 'Sideway 1633')
]



db.executemany(sql,val)

mydb.commit()

print(db.rowcount, "record inserted.")


