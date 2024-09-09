# SQLite - Sist. de gestión de bases de datos relacionales
import sqlite3

# ABRE la base de datos o CREA una base de datos si NO existe. Devuelve la ruta de enlace
conexion = sqlite3.connect("base_de_datos.db")

# Cierra la base de datos, debe cerrarse porque sino ocaciona problemas al volver a abrirla
conexion.close()