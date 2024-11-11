# create_table.py
from connection import connect

def create_table():
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                descripcion TEXT,
                precio DECIMAL NOT NULL,
                stock INT NOT NULL,
                categoria VARCHAR(30),
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        connection.commit()
        cursor.close()
        connection.close()
        print("Tabla creada exitosamente.")
    else:
        print("No se pudo conectar a la base de datos.")
