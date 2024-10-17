import mysql.connector
import csv
import pandas as pd


mydb = mysql.connector.connect(host = "bbch29avnyjqhx2niufi-mysql.services.clever-cloud.com", user = "uamuwfsdhltdwsmy", passwd = "NUFrO1KTqxCXyYJh8gYE", database = "bbch29avnyjqhx2niufi")

mycursor = mydb.cursor()

