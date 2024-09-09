# SQLite - Crear una tabla en nuestra base de datos
import sqlite3

# ABRE la base de datos o CREA una base de datos si NO existe. Devuelve la ruta de enlace
conexion = sqlite3.connect("base_de_datos.db")

# CURSOR crea un objeto que nos permite ejecutar sentencias SQL dentro de la base de datos
cursor = conexion.cursor()

# Introduce fila en la tabla PERSONA
cursor.execute("INSERT INTO PERSONAS VALUES ('Emanuel', 'Guaráz', 'Reynoso', 28)")

# Guarda definitivamente los cambios
conexion.commit()

# Cierra la base de datos, debe cerrarse porque sino ocaciona problemas al volver a abrirla
conexion.close()