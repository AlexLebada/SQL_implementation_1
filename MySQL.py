# Working with MySQL

import mysql.connector

mydb = mysql.connector.connect(host = "bbch29avnyjqhx2niufi-mysql.services.clever-cloud.com", user = "uamuwfsdhltdwsmy", passwd = "NUFrO1KTqxCXyYJh8gYE", database = "bbch29avnyjqhx2niufi")

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS customers")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [("John", "Highway 21"),
        ("Ana", "Highway 22"),
        ("George", "Low way 22"),
        ("George", "High way 30")
       ]
mycursor.executemany(sql, val)
mydb.commit()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address ='Highway 21'"
mycursor.execute(sql)
mydb.commit()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)