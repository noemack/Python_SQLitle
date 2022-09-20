# coding: ISO-8859-1
import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('databaseagre.db') # se define la base de datos
        conexion.execute('PRAGMA foreing_keys = ON') # para activar las llaves foráneas
        print('Conexión exitosa') # para comprobar si la conección es exitosa
        return conexion
    
    except Error:
        print(Error)
        
        
# se crean las tablas y se ingresan registros
def tabla(conexion):
    conexion.execute ("CREATE TABLE clientes (id integer PRIMARY KEY, nombre text, apellido text)")
    conexion.execute ("CREATE TABLE ordenes (id integer PRIMARY KEY, cliente_id integer, nombre_producto text, cantidad integer)")
    conexion.execute ("INSERT INTO clientes (id, nombre, apellido) VALUES (123, 'Manuel', 'Ramirez')")
    conexion.execute ("INSERT INTO clientes (id, nombre, apellido) VALUES (564, 'Maria', 'Perez')")
    conexion.execute ("INSERT INTO clientes (id, nombre, apellido) VALUES (555, 'Luis', 'Diaz')")
    conexion.execute ("INSERT INTO ordenes (cliente_id, nombre_producto, cantidad) VALUES (123, 'arroz', 2), (123, 'fideos', 3), (123, 'leche', 5), (123, 'huevos', 12)")
    conexion.execute ("INSERT INTO ordenes (cliente_id, nombre_producto, cantidad) VALUES (564, 'harina', 2), (564, 'huevos', 3), (564, 'azucar', 1), (564, 'chocolate', 1)")
    conexion.execute ("INSERT INTO ordenes (cliente_id, nombre_producto, cantidad) VALUES (555, 'pan', 2), (555, 'leche', 3), (555, 'azucar', 2), (555, 'huevos', 6)")
    conexion.commit()


# se define la funcion para realizar operaciones de agregación (COUNT, SUM, MAX, MIN, AVG, UPPER, LOWER, LENGTH)
def consultas(conexion):
    cursor = conexion.cursor()
    
    # datos almacenados en la tabla clientes
    consulta1 = "SELECT * FROM  clientes"
    
    # datos almacenados en la tabla ordenes
    consulta2 = "SELECT * FROM ordenes" 
    
    # cantidad de registros que están contenidos en la tabla ordenes
    consulta3 = "SELECT COUNT (*) FROM ordenes"
    
    # cantidad de registros que están contenidos en la tabla ordenes
    consulta4 = "SELECT COUNT (*) FROM clientes"
    
    # suma de la cantidad de productos de las ordenes
    consulta5 = "SELECT SUM (cantidad) FROM ordenes"
    
    # mayor número de cantidad de productos en las ordenes
    consulta6 = "SELECT MAX (cantidad) FROM ordenes"
    
    # menor número de cantidad de productos en las ordenes
    consulta7 = "SELECT MIN (cantidad) FROM ordenes"
    
    # promedio de la cantidad de productos de la tabla ordenes
    consulta8 = "SELECT AVG (cantidad) FROM ordenes"
    
    # cambiar a mayúsculas los nombres de los clientes
    consulta9 = "SELECT UPPER (nombre) FROM clientes"
    
    # cambiar a minúsculas los nombres de los clientes
    consulta10 = "SELECT LOWER (nombre) FROM clientes"
    
    # visualizar la longitud de cada uno de los nombres de los clientes
    consulta11 = "SELECT LENGTH (nombre) FROM clientes"
    
        
    # elegir la consulta para poder visualizar el resultado    
    cursor.execute(consulta1)
    filas = cursor.fetchall()
    
    for fila in filas:
        print (fila)    
        


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# se define la variable para almacenar la función conectar   
con = conectar()

# se llama a la funciones
tabla(con)
consultas(con)

# cerrar la conexión con la base de datos
con.close()
print("Conexión finalizada")     