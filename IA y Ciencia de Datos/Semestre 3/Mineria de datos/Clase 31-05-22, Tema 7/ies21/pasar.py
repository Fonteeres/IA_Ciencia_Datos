import pandas as pd

df = pd.read_csv('paises.csv')

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ies21"
)

mycursor = mydb.cursor()

for index, row in df.iterrows():
    SQL = "INSERT INTO paises VALUES({}, '{}')".format(row[0], row[1])
    mycursor.execute(SQL)

mydb.commit()

print("LISTO")