import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ohjelmisto1',
    autocommit=True
)
def location1(code):
    global point1
    sql = "SELECT latitude_deg, longitude_deg " \
          " FROM airport" \
          " WHERE ident = '" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for rivi in result:
        point1 = []
        point1.append(rivi[0])
        point1.append(rivi[1])
    return point1

def location2(code):
    global point2
    sql = "SELECT latitude_deg, longitude_deg " \
          " FROM airport" \
          " WHERE ident = '" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for rivi in result:
        point2 = []
        point2.append(rivi[0])
        point2.append(rivi[1])
    return point2

code1 = input("Anna ICAO-koodi1: ")
code2 = input("Anna ICAO-koodi2: ")

print(f"Maitten välinen etäisyys: "
      f"{geodesic(location1(code1), location2(code2)).km}km.")


