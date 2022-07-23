import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'ies_user',
    password = 'ies_pass',
    database = 'empresa'
)

micursor = midb.cursor()

misql = 'SELECT sector, nombre FROM sectores WHERE sector < 3 ORDER BY sector'

micursor.execute(misql)

sectores = micursor.fetchall()

for sector in sectores:
    print('{} - {}\n'.format(sector[0], sector[1]))

