
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ohjelmisto1',
    autocommit=True
)

def maatunnus_haku(FI):
    sql = " SELECT type, count(*)" \
          " FROM airport" \
          " WHERE airport.iso_country = '" + FI + "'" \
          " GROUP BY type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for rivi in result:
        print(f"Kenttä tyyppi: {rivi[0]}."
              f" Näitten määrä: {rivi[1]}.")

lol = input("Maatunnus: ")
maatunnus_haku(lol)