import psycopg2
from datetime import date, datetime

conn = psycopg2.connect("dbname= dht11 user=mike host=localhost password=mikeishere")

def create_table():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS measures (id SERIAL PRIMARY KEY,device varchar(45) NOT NULL, temperature integer NOT NULL, humidity integer NOT NULL, date date);')


def insert_table(device,temperature,humidity):
    with conn:
        with conn.cursor() as cursor:
            SQL = "INSERT INTO measures (device,temperature,humidity,date) VALUES(%s,%s,%s,(to_timestamp(%s, 'yyyy-mm-dd hh24:mi:ss'))) RETURNING True"
            data = (device,temperature,humidity,datetime.now())
            cursor.execute(SQL, data)

# def delete_table():
#     with conn:
#         with conn.cursor() as cursor:
#             SQL = "DELETE measures WHERE "