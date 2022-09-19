

import mysql.connector

mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ohjelmisto1',
    autocommit=True
    )

#sql = 'SELECT * FROM country WHERE iso_country='FI';'

sql = "SELECT * FROM country;"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
print("koko tulos lista:", result)
for row in result:
    print(row)