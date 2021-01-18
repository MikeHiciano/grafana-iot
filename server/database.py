import psycopg2
from datetime import date, datetime

conn = psycopg2.connect("dbname= dht11 user=postgres host=localhost")

def create_table():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS measures (id SERIAL PRIMARY KEY,device varchar(45) NOT NULL, temperature integer NOT NULL, humidity integer NOT NULL, date date, hour integer);')


def insert_table(device,temperature,humidity):
    with conn:
        with conn.cursor() as cursor:
            actual_date = date.today()
            actual_time = datetime.now()
            SQL = "INSERT INTO measures (device,temperature,humidity,date,hour) VALUES(%s,%s,%s,%s,%s) RETURNING True"
            data = (device,temperature,humidity,actual_date,int(actual_time.hour))
            cursor.execute(SQL, data)