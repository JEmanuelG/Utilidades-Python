# Series con modulo Pandas

# IMPORTA MODULO PANDAS
import pandas as pd

# CREA UNA SERIE DE UNA LISTA DE NÚMEROS
serie1 = pd.Series([3, 5, 7])
print(serie1)

# LISTAS QUE VAMOS A UTILIZAR PARA EJEMPLOS
asignaturas = ['Matemáticas', 'Física', 'Historia', 'Literatura']
notas_daniel = [8, 6, 9, 7]

# CREA UNA SERIE CON LAS NOTAS Y PASA LA LISTA DE ASIGNATURAS COMO ÍNDICE
serie_notas_daniel = pd.Series(notas_daniel, index=asignaturas)
print(serie_notas_daniel)

# MUESTRA UNA NOTA PASANDO SU ÍNDICE
print(serie_notas_daniel['Física'])

# MUETRA VALORES QUE CUMPLAN UNA CONDICION
# MUESTRA MATEMATICAS 8 E HISTORIA 9
print(serie_notas_daniel[serie_notas_daniel >= 8])

# NOMBRE LA SERIE
serie_notas_daniel.name = 'Notas de Daniel'

# NOMBRA LOS INDICES, ASIGNATURAS EN ESTE CASO
serie_notas_daniel.index.name = 'Asignaturas'
print(serie_notas_daniel)

# CONVIERTE UNA SERIE EN DICCIONARIO
diccionario = serie_notas_daniel.to_dict()
print(diccionario)

# CONVIERTE DICCIONARION EN SERE, PERO EN ESTA CONVERSION PIERDE LOS NOMBRES
serie_dic = pd.Series(diccionario)


# CREA OTRA SERIE PARA EJEMPLO
notas_ana = [9, 7, 9, 8]

serie_notas_ana = pd.Series(notas_ana, index=asignaturas)
print(serie_notas_ana)

# SE PUEDEN APLICAR OPERADORES MATEMATICOS
media_notas = (serie_notas_daniel + serie_notas_ana) / 2
print(media_notas)