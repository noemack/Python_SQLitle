# Python_SQLitle
Manejo de Bases de Datos básico utilizando Python y SQLitle, en editor Visual Studio Code

Utilizamos para este trabajo el gestor de base de datos SQLite, dado que el proyecto es considerablemente pequeño ya que sólo contiene funciones básicas

Si tienen interés pueden explorar la página con documentación oficial para encontrar más contenido referente a temas y métodos

[Python-SQlitle3](https://docs.python.org/es/3/library/sqlite3.html)

[SQlitle](https://www.sqlite.org/whentouse.html)

[Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)



## Herramientas

- Python
- SQLitle
- Visual Studio Code

> Tener en cuenta que en algunas partes el código puede estar comentado, quitar para probar las diferentes operaciones y funciones



## Esquema

> "ManejoBD", [Link](https://github.com/noemack/Python_SQLitle/blob/main/ManejoBD.py)

##### Conexión - Definición de la BD - Operaciones de tablas: crear, modificar, eliminar, ingresar registros, modificar registros, eliminar registros y consultar

---

> "AgregacionBD", [Link](https://github.com/noemack/Python_SQLitle/blob/main/AgregacionBD.py)

##### Conexión - Definición de la BD - Operaciones de agregación (COUNT, SUM, MAX, MIN, AVG, UPPER, LOWER, LENGTH)

---

> "ConjuntoBD", [Link](https://github.com/noemack/Python_SQLitle/blob/main/ConjuntoBD.py)

##### Conexión - Definición de la BD - Operaciones de conjuntos (INNER JOIN - LEFT JOIN)
> INNER JOIN: muestra como resultado la intersección de ambas tablas, sólo la intersección se mostrará en los resultados

> LETF JOIN: todos los valores de las columnas que seleccione de la tabla de la izquierda se incluirán en el resultado de la consulta, por lo que independientemente de que el valor coincida o no con la condición de combinación, se incluirá en el resultado. Por lo tanto, si se encuentran coincidencias, se mostrarán los valores correspondientes, de lo contrario visualizaremos NULL en los resultados

---

> "PandasBD", [Link](https://github.com/noemack/Python_SQLitle/blob/main/PandasBD.py)

##### Pandas: Read - Conexión - Creación de la BD - Exploración (columns, rename, info(), shape, isnull(), duplicated(), iloc, value_counts() y Consultas (pd.read_csv, pd.read_sql, pd.DataFrame, pd.crosstab)

> Librería Pandas: es una librería especializada en el manejo y análisis de estructuras de datos
> Algunas características:
> - Permite cargar datos, modelar, analizar, filtrar y manipular
> - Permite leer y escribir fácilmente ficheros en formato CSV, Excel y bases de datos SQL
> - Permite acceder a los datos mediante índices o nombres para filas y columnas
> - Permite trabajar con series temporales
> - Ofrece métodos para reordenar, dividir y combinar conjuntos de datos
> - Integrada con Matplotlib permite realizar gráficos de forma sencilla utilizando la función plot()

El set de datos "Dataset3.csv" fué obtenido del Catálogo de Datos de Kaggle: https://www.kaggle.com/datasets/babyoda/women-entrepreneurship-and-labor-force
(Informe Índice de Emprendimiento de Mujeres e Índice de Emprendimiento Global publicado en 2015)
