# Python_SQLitle
Manejo de Bases de Datos básico utilizando Python y SQLitle, en editor Visual Studio Code

Utilizamos para este trabajo el gestor de base de datos SQLite, dado que el proyecto es considerablemente pequeño ya que sólo contiene funciones básicas

Si tienen interés pueden explorar la página con documentación oficial para encontrar más contenido referente a temas y métodos

[Python-SQlitle3](https://docs.python.org/es/3/library/sqlite3.html)

[SQlitle](https://www.sqlite.org/whentouse.html)



## Herramientas

- Python
- SQLitle
- Visual Studio Code

> Tener en cuenta que en algunas partes el código puede estar comentado, quitar para probar las diferentes operaciones y funciones



## Esquema

> "ManejoBD", [Link](https://github.com/noemack/Python_SQLitle/blob/main/ManejoBD.py)

##### Conexión - Definición de la BD - Operaciones de tablas: crear, modificar, eliminar, ingresar registros, modificar registros, eliminar registros y consultar



> "AgregacionBD", [Link](https://github.com/noemack/Python_SQLitle/blob/main/AgregacionBD.py)

##### Conexión - Definición de la BD - Operaciones de agregación (COUNT, SUM, MAX, MIN, AVG, UPPER, LOWER, LENGTH)

> "ConjuntoBD", [Link](https://github.com/noemack/Python_SQLitle/blob/main/ConjuntoBD.py)

##### Conexión - Definición de la BD - Operaciones de conjuntos (INNER JOIN - LEFT JOIN)
> INNER JOIN: muestra como resultado la intersección de ambas tablas, sólo la intersección se mostrará en los resultados

> LETF JOIN: todos los valores de las columnas que seleccione de la tabla de la izquierda se incluirán en el resultado de la consulta, por lo que independientemente de que el valor coincida o no con la condición de combinación, se incluirá en el resultado. Por lo tanto, si se encuentran coincidencias, se mostrarán los valores correspondientes, de lo contrario visualizaremos NULL en los resultados

