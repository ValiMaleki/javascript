import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2020',
    autocommit=True
)
def get_airports(ident):
    sql = f"""SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
              FROM airport
              WHERE ident = '{ident}'"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

get_airports('EFHK')
