# SQLite3 - Borrar datos de tabla PERSONAS
import sqlite3

#CONECTA CON DB
conexion = sqlite3.connect("base_de_datos.db")

cursor = conexion.cursor()

# BORRA DATOS SEGUN CONDICIÓN, SI NO SE PONE CONDICIÓN BORRA TODO
cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Lali'")

# GUARDA CAMBIOS DEFINITVAMENTE
conexion.commit()

#CIERRA DB
conexion.close()
