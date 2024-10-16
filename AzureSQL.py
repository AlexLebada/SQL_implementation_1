import pyodbc
import pandas as pd
#from credential import username, password

server = 'tcp:testtest123123.database.windows.net'
database = 'test'
username = 'alexlebada'
password = 'Happyness123@'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+', 1433;DATABASE='+database+';UID='+username+';PWD='+password+';ENCRYPT=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = pyodbc.connect(connection_string)

conn.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
conn.execute("""INSERT INTO customers (name, address) VALUES
('Mike', 20),
('John', 32),
('Sanda', 35),
('Julian', 40),
('Joanna', 50)
""")
conn.commit()