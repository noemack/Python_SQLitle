# coding: ISO-8859-1
from cgi import print_arguments
import sqlite3
from sqlite3 import Error, Row


# se define la función conectar
def conectar():
    try:
        conexion = sqlite3.connect('myBD.db') # se define la base de datos
        conexion.execute('PRAGMA foreing_keys = ON') # para activar las llaves foráneas
        print('Conexión establecida') # para comprobar si la conección es exitosa
        return conexion
    
    except Error:
        print('Error')

# se crean las tablas        
def crearTabla(conexion):
    conexion.execute('CREATE TABLE estudiante (matricula integer PRIMARY KEY, nombre text not null, apellidos text not null, fechaInicio text not null, promedio real)')
    conexion.execute('CREATE TABLE carrera (id integer PRIMARY KEY, nombre text not null, estudiante integer)')
    conexion.execute('CREATE TABLE datosContacto (id integer PRIAMRY KEY , estudiante integer, telefono1 text , telefono2 text, correo text, CONSTRAINT fk_contactoEstudiante FOREIGN KEY (estudiante) REFERENCES estudiante (matricula))')
    print('Tablas creadas')         

# se define la función para modificar una tabla
def modificarTabla(conexion):
    conexion.execute('ALTER TABLE estudiante ADD COLUMN carrera text not null')
    conexion.execute('ALTER TABLE estudiante ADD COLUMN grado integer not null')
    conexion.execute('ALTER TABLE estudiante ADD COLUMN grupo text not null')
    conexion.commit() # método para guardar
    print('Tabla modificada')         
    
# se define la función para eliminar una tabla
def eliminarTabla(conexion):
    conexion.execute('DROP TABLE IF EXISTS carrera')
    conexion.commit()
    print('Tabla eliminada')

# se define la función para ingresan registros
def insertarRegistro(conexion):
    conexion.execute("INSERT INTO estudiante (nombre, apellidos, fechaInicio, promedio, carrera, grado, grupo) VALUES ('Ana', 'Romero Cardozo', '2000-06-09', 8.75, 'Ingenieria Industrial', 1, 'G')")
    conexion.execute("INSERT INTO estudiante (nombre, apellidos, fechaInicio, promedio, carrera, grado, grupo) VALUES ('Maria', 'Díaz Lemos', '2008-01-15', 9.2, 'Licenciatura en Enfermeria', 6, 'B')")
    conexion.execute("INSERT INTO estudiante (nombre, apellidos, fechaInicio, promedio, carrera, grado, grupo) VALUES ('Juan', 'Ruiz Díaz', '2008-02-15', 8.2, 'Licenciatura en Enfermeria', 6, 'B')")
    conexion.execute("INSERT INTO estudiante (nombre, apellidos, fechaInicio, promedio, carrera, grado, grupo) VALUES ('Daniel', 'Rodríguez Ford', '2006-03-20', 7.5, 'Logística', 5, 'C')")
    conexion.execute("INSERT INTO estudiante (nombre, apellidos, fechaInicio, promedio, carrera, grado, grupo) VALUES ('Valeria', 'Rodríguez Suarez', '2001-06-02', 8.2, 'Informática', 4, 'B')")
    conexion.execute("INSERT INTO datosContacto (estudiante, telefono1, telefono2, correo) VALUES (1, '8331234567', '5552334455', 'anaromero@gmail.com')")
    conexion.execute("INSERT INTO datosContacto (estudiante, telefono1, telefono2, correo) VALUES (2, '0554564567', '1111234567', 'mariadiaz@gmail.com')")
    conexion.execute("INSERT INTO datosContacto (estudiante, telefono1, telefono2, correo) VALUES (3, '4499456733', '4455662233', 'juaruiz@gmail.com')")
    conexion.execute("INSERT INTO datosContacto (estudiante, telefono1, telefono2, correo) VALUES (4, '1234098765', '4536267890', 'danielrodriguez@gmail.com')")
    conexion.execute("INSERT INTO datosContacto (estudiante, telefono1, telefono2, correo) VALUES (5, '8899446612', '9988771122', 'valeriarodriguez@gmail.com')")
    conexion.commit()
    print('Ingresos de registros completado')

# se define la función para modificar registros
def modificarRegistro(conexion, matricula, nombre, telefono):
    conexion.execute ("UPDATE estudiante SET nombre = '"+nombre+"' WHERE matricula = "+str(matricula))
    conexion.execute ("UPDATE datosContacto SET telefono1 = '"+telefono+"' WHERE estudiante = "+str(matricula))
    conexion.commit()
    print('Registros modificados')

# se define la función para eliminar registros
def eliminarRegistro(conexion):
    conexion.execute ("DELETE FROM datosContacto WHERE estudiante = 1")
    conexion.execute ("DELETE FROM datosContacto WHERE estudiante = 2")
    conexion.execute ("DELETE FROM estudiante WHERE matricula = 2")
    conexion.commit()
    print('Registros eliminados')
    
# se definen las consultas
def consulta(conexion):
    cursor = conexion.cursor()
    cursor.execute ("SELECT * FROM estudiante WHERE promedio >8 and carrera = 'Ingenieria Industrial'")
    filas = cursor.fetchall()
    print('Consulta: estudiante de la carrera Ingeniería Industrial cuyo promedio sea mayor a 8')
    print(filas)
    
    
        
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# se define la variable para almacenar la función conectar        
con = conectar()

# se llama a la funciones

crearTabla(con)
modificarTabla(con)          
eliminarTabla(con)
insertarRegistro(con)
modificarRegistro(con, 1, 'Juan', '5551234567')
eliminarRegistro(con)
consulta(con)

# cerrar la conexión con la base de datos
con.close()
print("Conexión finalizada")