# SQLite - Actualizar datos
import sqlite3

conexion = sqlite3.connect("base_de_datos.db")

cursor = conexion.cursor()

cursor.execute ("UPDATE PERSONAS SET edad = 4 WHERE nombre = 'Tutuca'")

conexion.commit()
conexion.close()