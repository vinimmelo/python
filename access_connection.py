import pyodbc

conn = pyodbc.connect(r'DRIVER={SQL Server}; DBQ=C:\Users\brmelovi\NESTLE\colombia-ZD30 - Documentos\Database\Registros Claims.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Doc9k')

for row in cursor.fetchall():
    print (row)
