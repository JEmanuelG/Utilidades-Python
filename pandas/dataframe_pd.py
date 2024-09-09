# DataFrames con Pandas

# IMPORTA MODULO PANDAS
import pandas as pd

# IMPORTA MODULO WEBBROWSER
import webbrowser

# CREA VARIABLE CON URL DE UN SITIO WEB
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'

# ABRE EL SITIO WEB EN EL NAVEGADOR
webbrowser.open(website)

# TOMA DATOS DEL PORTAPAPELES (LO QUE COPIAMOS Y PEGAMOS) Y LO GUARDA EN UNA VARIABLE DATAFRAME
dataframe_nba = pd.read_clipboard()
print(dataframe_nba)

# MUESTRA LAS COLUMNAS QUE TIENE EL DATAFRAME
print(dataframe_nba.columns)

# ACCEDE A LA COLUMNA 'Campeón del Oeste' DEL DATAFRAME
print(dataframe_nba['Campeón del Oeste'])

# ACCEDE A LA FILA CON INDICE 5 MEDIANTE .LOC
print(dataframe_nba.loc[5])

# ACCEDE A LAS FILAS DEL 0 AL 3 DE LAS COLUMNAS ['Campeón del Oeste','Resultado']
print(dataframe_nba.loc[0:3, ['Campeón del Oeste','Resultado']])


# DEVUELVE LAS 3 PRIMERAS FILAS DESDE LA CABECERA
print(dataframe_nba.head(3))

# DEVUELVE LAS ULTIMAS 2 FILAS DESDE ATRAS
print(dataframe_nba.tail(2))

# LISTA PARA CREAR DICCIONARIO PARA EJEMPLO
list_asignatura = ['matematicas', 'historia', 'fisica']
list_notas = [8,7,9]

# CREA DICCIONARIO CON LISTAS
diccionario = {'Asignaturas':list_asignatura, 'Notas':list_notas}

# CREA DATAFRAME A PARTIR DE UN DICCIONARIO
dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)
