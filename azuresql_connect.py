"""
Script to connect to Azure SQL DB
Reference: https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connect-query-python
"""


import pyodbc

server = '<server>.database.windows.net'
database = '<database>'
username = '<username>'
password = '<password>'
driver = '{ODBC Driver 13 for SQL Server}'  # check in the ODBC Client for driver version
cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
cursor.execute("select top 10 col1 from table1 where col1 = '1234'")
row = cursor.fetchone()

while row:
    print(str(row[0]))
    # print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
else:
    print('No Data')
