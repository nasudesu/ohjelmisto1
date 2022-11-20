import json
import mysql.connector
from flask import Flask, Response

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ohjelmisto1',
    autocommit=True
)

app = Flask(__name__)


@app.route("/kenttä/<icao>")
def airport(icao):
    try:
        sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{icao}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for rivi in result:
                response_dict = {"icao": rivi[0], "Lentokentän Nimi": rivi[1], "Lentokentän kaupunki": rivi[2]}
                response_json = json.dumps(response_dict)
                return Response(response=response_json, status=200, mimetype="application/json")
    except TypeError:
        response_json = json.dumps('"message": Invalid parameters missing?')
        return Response(response=response_json, status=400)


@app.errorhandler(500)
def page_not_found(error):
    error_text = str(error)
    response_json = json.dumps({"error": error_text})
    return Response(response=response_json, status=500, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
