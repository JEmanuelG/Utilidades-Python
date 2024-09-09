# SQLite - Insertar varios registros a la vez en la tabla
import sqlite3

# ABRE la base de datos o CREA una base de datos si NO existe. Devuelve la ruta de enlace
conexion = sqlite3.connect("base_de_datos.db")

# CURSOR crea un objeto que nos permite ejecutar sentencias SQL dentro de la base de datos
cursor = conexion.cursor()

# Crea lista de personas
list_personas = [("Melany","Pedraza", "Tarquino", 25),
                 ("Tutuca", "Guaráz", "Pedraza", 3),
                 ("Lali", "Pedraza", "Tarquino", 10)]

# Inserta los registros, EXECUTEMANY se ejecuta varias veces, segun la cant de elementos que contiene la lista
cursor.executemany("INSERT INTO PERSONAS VALUES (?, ?, ?, ?)", list_personas)

# Guarda definitivamente los cambios
conexion.commit()

# Cierra la base de datos, debe cerrarse porque sino ocaciona problemas al volver a abrirla
conexion.close()