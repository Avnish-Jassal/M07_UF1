# read.py
from connection import connect

def read_productos():
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        for producto in productos:
            print(producto)
        cursor.close()
        connection.close()
    else:
        print("No se pudo conectar a la base de datos.")
