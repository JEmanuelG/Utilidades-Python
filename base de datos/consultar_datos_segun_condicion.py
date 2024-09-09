# SQLite3 - Consultar datos que cumplan una determinada condición
import sqlite3

# Abre DB o crea una si no existe
conexion = sqlite3.connect("base_de_datos.db")

# Crea cursor para poder ejecutar sentencias de SQL
cursor = conexion.cursor()

# Consulta según condición. Con WHERE ponemos la condición
cursor.execute("SELECT * FROM PERSONAS WHERE edad > 20")

# Guarada los datos en la variable. FETCHALL toma los datos de la ejecución anterior
personas_mas_20 = cursor.fetchall()

# itera sobre personas_mas_20 y muestra elementos
for persona in personas_mas_20:
    print(persona)

print(personas_mas_20)

# Cierra base de datos
conexion.close()