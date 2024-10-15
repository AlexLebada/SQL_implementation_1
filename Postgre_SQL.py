import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="happyness", port=5432)

cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR )
""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1, 'Mike', 20, 'm'),
(2, 'John', 32, 'm'),
(3, 'Sanda', 35, 'f'),
(4, 'Julian', 40, 'm'),
(5, 'Joanna', 50, 'f')
""")

conn.commit()

cur.close()
conn.close()