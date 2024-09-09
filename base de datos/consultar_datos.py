# SQLite - Crear una tabla en nuestra base de datos
import sqlite3

# ABRE la base de datos o CREA una base de datos si NO existe. Devuelve la ruta de enlace
conexion = sqlite3.connect("base_de_datos.db")

# CURSOR crea un objeto que nos permite ejecutar sentencias SQL dentro de la base de datos
cursor = conexion.cursor()

# Consulta todas las filas y columnas (con el *) de la tabla PERSONAS
cursor.execute("SELECT * FROM PERSONAS")

# Guarda los datos consultados en la var personas. FETCHALL toma los resultado de la ajecución anterior
personas = cursor.fetchall()

#Itera sobre la lista personas y muestra sus datos
for persona in personas:
    print(persona)

# Cierra la base de datos, debe cerrarse porque sino ocaciona problemas al volver a abrirla
conexion.close()