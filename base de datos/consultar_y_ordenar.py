# SQLite3 - Consultar y ordenar datos segun columna
import sqlite3

# Conecta con DB
conexion = sqlite3.connect("base_de_datos.db")

cursor = conexion.cursor()

# Consulta y ordena los datos de la columna edad con ORDER BY 
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")

# Toma y guarda los datos en una lista
personas = cursor.fetchall()

# Itera y muestras los datos de personas
for persona in personas:
    print(persona)

# Cierra DB
conexion.close()