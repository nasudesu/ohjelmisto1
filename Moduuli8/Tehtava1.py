import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ohjelmisto1',
    autocommit=True
)

def koodihaku(code):
    sql = "SELECT name, municipality " \
          " FROM airport" \
          " WHERE ident = '" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for rivi in result:
            print(f"Lentokentän nimi: {rivi[0]}. Lentokentän kaupunki: {rivi[1]}.")

code = input("Anna ICAO-koodi: ")
koodihaku(code)
