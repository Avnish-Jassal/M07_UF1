
from numpy import integer

from create_table import create_table
from create import create_producto
from read import read_productos
from update import update_producto
from delete import delete_producto

def main():
    # Crear la tabla si no existe
    create_table()

    while True:
        try:
            # Menú de opciones
            print("\nMenú de opciones:")
            print("1. Crear producto")
            print("2. Leer productos")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":  # Crear producto
                nombre = input("Nombre del producto: ")
                descripcion = input("Descripción: ")
                precio = int(input("Precio: "))
                stock = int(input("Stock: "))
                categoria = input("Categoría: ")
                create_producto(nombre, descripcion, precio, stock, categoria)

            elif opcion == "2":  # Leer productos
                read_productos()

            elif opcion == "3":  # Actualizar producto
                id = int(input("ID del producto a actualizar: "))
                nombre = input("Nuevo nombre (deja vacío para no cambiar): ") or None
                descripcion = input("Nueva descripción (deja vacío para no cambiar): ") or None
                precio = input("Nuevo precio (deja vacío para no cambiar): ")
                precio = float(precio) if precio else None
                stock = input("Nuevo stock (deja vacío para no cambiar): ")
                stock = int(stock) if stock else None
                categoria = input("Nueva categoría (deja vacío para no cambiar): ") or None
                update_producto(id, nombre, descripcion, precio, stock, categoria)

            elif opcion == "4":  # Eliminar producto
                id = int(input("ID del producto a eliminar: "))
                delete_producto(id)

            elif opcion == "5":  # Salir
                print("Saliendo del programa...")
                break

            else:  # Opción inválida
                print("Opción no válida. Intenta de nuevo.")

        except KeyboardInterrupt:  # Captura el Ctrl+C
            print("\nProceso interrumpido por el usuario.")
            break  # Sale del ciclo de menú

if __name__ == "__main__":
    main()
