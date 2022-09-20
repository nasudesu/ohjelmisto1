import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ohjelmisto1',
         autocommit=True
         )


icao = input("Anna lentokenttä ICAO-Koodi: ")
sql = "SELECT name , municipality FROM airport WHERE ident = '" + icao + "'"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")