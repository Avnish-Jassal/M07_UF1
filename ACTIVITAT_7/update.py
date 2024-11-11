# update.py
from connection import connect

def update_producto(id, nombre=None, descripcion=None, precio=None, stock=None, categoria=None):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        query = '''
            UPDATE productos
            SET nombre = COALESCE(%s, nombre),
                descripcion = COALESCE(%s, descripcion),
                precio = COALESCE(%s, precio),
                stock = COALESCE(%s, stock),
                categoria = COALESCE(%s, categoria)
            WHERE id = %s
        '''
        cursor.execute(query, (nombre, descripcion, precio, stock, categoria, id))
        connection.commit()
        cursor.close()
        connection.close()
        print("Producto actualizado exitosamente.")
    else:
        print("No se pudo conectar a la base de datos.")
