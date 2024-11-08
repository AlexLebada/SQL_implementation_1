#Establish Azure database - python ODBC connection
# Extract from csv file, the columns dinamically and transfer them in SQL database
import pyodbc
import csv
import pandas as pd

server = 'tcp:testtest123123.database.windows.net'
database = 'test'
username = '#####'
password = '#####'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+', 1433;DATABASE='+database+';UID='+username+';PWD='+password+';ENCRYPT=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

data = pd.read_csv("titanic.csv")
column_names = list(data.columns)
cleaned_column_names = [element.replace('.', '') for element in column_names]

column_len = len(column_names)
list_column_names = [[] for _ in range(column_len)]

modified_column_types = []
column_types = data.dtypes.tolist()
# Add more data types if necessary
for col_type in column_types:
    if col_type == 'int64':
        modified_column_types.append('INT')
    elif col_type == 'object':
        modified_column_types.append('VARCHAR(255)')
    elif col_type == 'float64':
        modified_column_types.append('FLOAT')
    else:
        modified_column_types.append(str(col_type))  # Handle other types if needed

#print(modified_column_types)

combined_string = ""
combined_half_string = ""

# Use a for loop with zip to iterate over both lists
for name, dtype in zip(cleaned_column_names, modified_column_types):
    # Combine the column name and type into a formatted string
    combined_string += f"{name} {dtype}, "  # Add a comma for separation
    combined_half_string += f"{name}, "
# Remove the last comma and space for clean output
combined_string = combined_string[:-2]  # Remove the trailing comma and space
combined_half_string = combined_half_string[:-2]
# Print the final combined string
#print(combined_string)

cursor.execute("""CREATE TABLE titanic (ID int NOT NULL PRIMARY KEY IDENTITY, """+combined_string+""");
""")
#cursor.execute("DROP TABLE titanic")
conn.commit()



filename = "titanic.csv"
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    a = next(csvreader)
    for row in csvreader:
        for col in range(len(column_names)):
                list_column_names[col] = row[col]
        combined_string_2 = ""
        # Use loop to concatenate 2 lists, element by element
        i=0
        clean_list_column_names = [element.replace("'", "") for element in list_column_names]
        for name in clean_list_column_names:
            # Combine the column name and type into a formatted string
            if modified_column_types[i] == 'VARCHAR(255)':
                combined_string_2 += f"'{name}', "  # Add a comma for separation
            elif ((modified_column_types[i] == 'INT') or (modified_column_types[i] == 'FLOAT')) and (name == ''):
                combined_string_2 += "NULL, "
            else:
                combined_string_2 += f"{name}, "  # Add a comma for separation
            i=i+1
        combined_string_2 = combined_string_2[:-2]
        #print(combined_string_2)
        cursor.execute("INSERT INTO titanic (" + combined_half_string + ") VALUES (" + combined_string_2 + ") ")
        cursor.commit()



