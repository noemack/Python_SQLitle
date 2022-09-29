# coding: ISO-8859-1
import sqlite3
from sqlite3 import Error

# se define la función conectar
def conectar():
    try:
        conexion = sqlite3.connect('mydatabasejoin.db') # se define la base de datos
        conexion.execute('PRAGMA foreing_keys = ON') # para activar las llaves foráneas
        print('Conexión exitosa') # para comprobar si la conexión es exitosa
        return conexion
    
    except Error:
        print('Error')

# se crean las tablas        
def crearTabla(conexion):
    conexion.execute('CREATE TABLE cliente (cedula integer PRIMARY KEY, nombre text not null, apellidos text not null, fechaInicio text not null, ciudad text)')
    conexion.execute('CREATE TABLE datosContacto (id integer PRIAMRY KEY , cliente integer, telefono1 text , telefono2 text, correo text, CONSTRAINT fk_contactoCliente FOREIGN KEY (cliente) REFERENCES cliente (cedula))')
            

# se define la función para modificar una tabla
def modificarTabla(conexion):
    conexion.execute('ALTER TABLE cliente ADD COLUMN direccion text not null')
    conexion.execute('ALTER TABLE cliente ADD COLUMN pais integer not null')
    conexion.execute('ALTER TABLE cliente ADD COLUMN vendedor text not null')
    conexion.commit() # método para guardar


# se define la función para ingresan registros
def insertarRegistro(conexion):
    conexion.execute("INSERT INTO cliente (nombre, apellidos, fechaInicio, ciudad, direccion, pais, vendedor) VALUES ('Juan', 'Rodriguez Perez', '2022-06-09', 'San José', 'Camino Ibiray 234', 'Uruguay', 'Ana')")
    conexion.execute("INSERT INTO cliente (nombre, apellidos, fechaInicio, ciudad, direccion, pais, vendedor) VALUES ('Maria', 'Cruz Velazquez', '20022-01-15', 'Colonia', 'Calle 34', 'Uruguay', 'Dario')")
    conexion.execute("INSERT INTO cliente (nombre, apellidos, fechaInicio, ciudad, direccion, pais, vendedor) VALUES ('David', 'Sanchez Torres', '2021-12-09', 'Sevilla', 'Plaza de San Francisco', 'España', 'Ana')")
    conexion.execute("INSERT INTO cliente (nombre, apellidos, fechaInicio, ciudad, direccion, pais, vendedor) VALUES ('Jose', 'Montero Cruz', '2022-02-05', 'Madrid', 'Calle Orizaba 49', 'España', 'Luis')")
    conexion.execute("INSERT INTO datosContacto (cliente, telefono1, telefono2, correo) VALUES (1, '8331234567', '5552334455', 'juanrodriguez@gmail.com')")
    conexion.execute("INSERT INTO datosContacto (cliente, telefono1, telefono2, correo) VALUES (2, '0554564567', '1111234567', 'mariacruz@hotmail.com')")
    conexion.commit()
    

# se definen las consultas
def consulta(conexion):
    cursor = conexion.cursor()
    cursor.execute ("SELECT * FROM cliente")
    filas = cursor.fetchall()
    print('Tabla Cliente:')
    for row in filas: 
        print(row, '\n')

def consulta2(conexion):
    cursor = conexion.cursor()
    cursor.execute ("SELECT * FROM datosContacto")
    filas = cursor.fetchall()
    print('Tabla datosContacto:')
    for row in filas: 
        print(row, '\n')
        
def consulta3(conexion):
    cursor = conexion.cursor()
    cursor.execute ("SELECT cedula, apellidos FROM cliente WHERE pais = 'España'")
    filas = cursor.fetchall()
    print('Clientes de España:')
    for row in filas: 
        print(row, '\n')


# se define la función para realizar operaciones de conjuntos entre tablas independientes (LEFT JOIN, INNER JOIN)
def conjuntos(conexion):
    cursor = conexion.cursor()
    
    # INNER JOIN: muestra como resultado la intersección de ambas tablas, (sólo la intersección se mostrará en los resultados)
    # ¿cuáles son los clientes que cuentan con datos en la tabla de datos de contacto?
    cursor.execute ("SELECT nombre, apellidos FROM cliente JOIN datosContacto ON cliente.cedula = datosContacto.cliente")
    
    # LEFT JOIN: si no existe ninguna coincidencia para alguna de las filas de la tabla de la izquierda, de igual forma todos los resultados de la primera tabla se muestran
    # la tabla datosContacto aparece luego del LEFT JOIN, por lo tanto, si se encuentran coincidencias, se mostrarán los valores correspondientes, 
    # de lo contario aparecerá NULL en los resultados
    # cursor.execute ("SELECT cliente.apellidos as 'Cliente', datosContacto.correo as 'Mail' FROM cliente LEFT JOIN datosContacto ON datosContacto.cliente = cliente.cedula")

    
    filas = cursor.fetchall()
    print ('Resultado consulta')
    for row in filas: 
        print(row)
           
    
        
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# se define la variable para almacenar la función conectar        
con = conectar()

# se llama a la funciones

crearTabla(con)
modificarTabla(con)          
insertarRegistro(con)
consulta(con)
consulta2(con)
consulta3(con)
conjuntos(con)

# cerrar la conexión con la base de datos
con.close()
print("Conexión finalizada")
