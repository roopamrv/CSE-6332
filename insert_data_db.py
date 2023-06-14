import pyodbc
server = 'cse6332-db-server.database.windows.net'
username = 'cse6332-user'
password = 'Test@123'
database = 'cse6332'
driver= '{ODBC Driver 17 for SQL Server}'
import csv

with open('people.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

# with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
#         row = cursor.fetchone()
#         while row:
#             print (str(row[0]) + " " + str(row[1]))
#             row = cursor.fetchone()