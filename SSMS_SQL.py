import pyodbc

try:
    conn = pyodbc.connect("Driver={SQL Server};"
                         "Server=ALEXANDRU\TEW_SQLEXPRESS;"
                         "Database=test;"
                         "Trusted_Connection=True;")
    conn.autocommit=True
    print('Connected to database')
except pyodbc.Error as ex:
    print('Connection failed',ex)

conn.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
conn.execute("""INSERT INTO customers (name, address) VALUES
('Mike', 20),
('John', 32),
('Sanda', 35),
('Julian', 40),
('Joanna', 50)
""")


