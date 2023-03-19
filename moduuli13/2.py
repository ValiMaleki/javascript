import mysql.connector
from flask import Flask, Response
import json

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2020',
    autocommit=True
)

app = Flask(__name__)

@app.route('/airport/<icao>')
def get_airports(icao):
    try:
        sql = f"""SELECT  name, municipality
              FROM airport
                  WHERE ident = '{icao}'"""
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchall()

        if len(result) > 0:
            response = {
                "ICAO": icao,
                "Name:": result[0]['name'],
                "Location": result[0]['municipality']
            }
            return response
        else:
            response = {
                "message": "Airport not found",
                "status": 404
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response, status=404, mimetype="application/json")
            return http_response

    except ValueError:
        response = {
            "message": "Invalid endpoint",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
