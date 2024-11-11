# create.py
from connection import connect

def create_producto(nombre, descripcion, precio, stock, categoria):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, precio, stock, categoria)
            VALUES (%s, %s, %s, %s, %s)
        ''', (nombre, descripcion, precio, stock, categoria))
        connection.commit()
        cursor.close()
        connection.close()
        print("Producto creado exitosamente.")
    else:
        print("No se pudo conectar a la base de datos.")
