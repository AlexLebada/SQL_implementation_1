Connection files for:
        - MySQL: mysql.connector lib
        - PostgreSQL: psycopg2 lib
        - SSMS: pyodbc

AzureSQL.py is the main program where :
        - I establish connection with Azure database through ODBC driver and pyodbc lib.
        - I import a csv with any no. of columns and data type, and transfer it to Azure database
