# delete.py
from connection import connect

def delete_producto(id):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM productos WHERE id = %s', (id,))
        connection.commit()
        cursor.close()
        connection.close()
        print("Producto eliminado exitosamente.")
    else:
        print("No se pudo conectar a la base de datos.")
