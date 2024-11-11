1. Create (Crear)
La operación Create permite añadir nuevos registros (en este caso, productos) a la base de datos. Al ejecutar esta operación, el usuario puede ingresar los detalles del producto, como su nombre, descripción, precio, stock, y categoría
![image](https://github.com/user-attachments/assets/88e22cd9-6d64-4bfa-9d10-4b47a1b92219)
Aqui vemos mi ejepmlo mas en especifico.

2. Read (Leer)
   
La operación Read permite ver todos los registros existentes en la tabla productos. Al ejecutarla, se obtiene una lista de todos los productos con sus respectivos detalles almacenados en la base de datos. En mi caso utilizo el cursor.fetchall()
Cuando haces una consulta SQL con un cursor, los datos devueltos se almacenan en este cursor, y fetchall() se usa para recuperar todos los resultados en una sola llamada
![image](https://github.com/user-attachments/assets/e4685f0e-5d25-44e1-b590-897191029e3d)
Este es mi ejemplo

3. Update (Actualizar)
La operación Update permite modificar los detalles de un producto existente en la base de datos. COALESCE es una función de SQL que se utiliza para manejar valores nulos. Su principal función es devolver el primer valor no nulo de una lista de expresiones
![image](https://github.com/user-attachments/assets/7a49778a-edac-4bf4-94c4-f91e52c3653f)
Este es mi ejepmlo

4. Delete (Eliminar)
La operación Delete permite eliminar un producto de la base de datos utilizando su id. Al ejecutar esta operación, el registro del producto es eliminado permanentemente de la tabla productos.
![image](https://github.com/user-attachments/assets/0d3d0c21-dbc3-4382-aa9d-00d656277290)
