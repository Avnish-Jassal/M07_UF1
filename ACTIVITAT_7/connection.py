# connection.py
import psycopg2

def connect():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
