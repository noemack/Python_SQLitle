# importar la libreria de pandas y sqlite3, (en el caso de que la librería no esté realizar comando: pip install pandas)
import pandas as pd
import sqlite3

# read, método de pandas para leer un archivo csv
data = pd.read_csv('Dataset3.csv', sep= ';')
print(data)

# conexión y creación de la base de datos womens
con = sqlite3.connect ('womens.db')
data.to_sql ('class', con, if_exists= 'replace', index= False) # tabla , parámetro de conexión y validación si existe
cursor = con.cursor() # método cursor

# exploración
consulta = "SELECT * FROM class"
data = pd.read_sql (consulta, con)

# encabezados
print('Encabezados: ')
print (data.columns, '\n')

# cambio de nombre de columnas: Level of development, European Union Membership
data.rename(columns={'Level of development': 'Level_of_development', 'European Union Membership':'European_Union_Membership'},
               inplace=True)
print('Cambio de nombre de columnas: Level of development y European Union Membership: ')
print(data.columns, '\n')

# información general
print('Información general: ')
print(data.info(), '\n')

# dimensión
print('Dimensionalidad: ')
print(data.shape, '\n')

# datos nulos
print('Datos nulos?')
print(data.isnull().sum().any(), '\n')
print(data.isnull().all(), '\n') # se aplica a las columnas
print(data.isnull().all(axis=1), '\n') # se aplica a las filas

# buscar duplicados
print('Duplicados?')
print(data.duplicated().value_counts, '\n')

# primera y última fila
print('Primera y última fila: ')
print(data.iloc[0])
print(data.iloc[-1], '\n')

# visualización de todos los países
print ('Países: ')
print(data.Country.value_counts(), '\n')


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# consultas

# listar los paises: Uruguay, Brazil y Argentina
consulta1 = "SELECT * FROM class  WHERE Country in ('Uruguay', 'Brazil', 'Argentina')"

# cual es el pais con el índice de inflación más alto?
consulta2 = "SELECT Country, Inflation_rate FROM class ORDER BY Inflation_rate DESC LIMIT 1"

# cual es el pais con el índice de inflación más bajo?
consulta3 = "SELECT Country, Inflation_rate FROM class ORDER BY Inflation_rate ASC LIMIT 1"

# país con índice de emprendimiento de mujeres más alto
consulta4 = "SELECT Country, Women_Entrepreneurship_Index FROM class ORDER BY Women_Entrepreneurship_Index DESC LIMIT 1"

# país con índice de emprendimiento de mujeres más bajo
consulta5 = "SELECT Country, Women_Entrepreneurship_Index FROM class ORDER BY Women_Entrepreneurship_Index ASC LIMIT 1"

# país con la tasa de índice de emprendimiento más bajo
consulta6 = "SELECT Country, Entrepreneurship_Index FROM class ORDER BY Entrepreneurship_Index ASC LIMIT 1"


cursor.execute(consulta1)

filas = cursor.fetchall()
print ('Resultado de la consulta')
for fila in filas:
    print(fila, '\n')


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Otras consultas

# Contando los miembros y no miembros de la UE
consulta7 = pd.DataFrame(data.groupby('European_Union_Membership').European_Union_Membership.count())
print('Miembros y no miembros de la UE: ')
print(consulta7, '\n')
 
# consulta con tabulación cruzada entre miembros de la UE y el nivel de desarrollo
consulta8 = pd.crosstab(data['European_Union_Membership'],data['Level_of_development'])
print('Tabulación cruzada entre miembros de la UE y el nivel de desarrollo: ')
print(consulta8, '\n')


# cerrar la conexión con la base de datos
con.close()
print("Conexión finalizada")
