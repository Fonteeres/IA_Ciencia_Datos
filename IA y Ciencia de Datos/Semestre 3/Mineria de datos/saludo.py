
import pyodbc
import pandas as pd
server = 'GINO-PC-FIJA'
base = 'Ventas2'
Cadena = "DRIVER=ODBC Driver 17 for SQL Server;SERVER= {};DATABASE={};Trusted_Connection=yes".format(server,base)
""" try:
    cnxn = pyodbc.connect(Cadena)
    cursor = cnxn.execute()
except Exception as e:
        print(e)
finally:
    print('PUDE INSERTAR')  """

cnxn = pyodbc.connect(Cadena)
cursor = cnxn.cursor()

query = "SELECT * FROM marcas;"
df = pd.read_sql(query, cnxn)
print(df.head(26))

""" cursor.execute("SELECT * FROM marcas")
myresult = cursor.fetchall()
for x in myresult:
    print(x) """

