import mysql.connector

mydb = mysql.connector.connect(host = "bbch29avnyjqhx2niufi-mysql.services.clever-cloud.com", user = "uamuwfsdhltdwsmy", passwd = "NUFrO1KTqxCXyYJh8gYE", database = "bbch29avnyjqhx2niufi")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers WHERE name = 'George' ")
myresult = mycursor.fetchall()

mycursor.execute("SELECT * FROM customers LIMIT 5")
mydb.commit()