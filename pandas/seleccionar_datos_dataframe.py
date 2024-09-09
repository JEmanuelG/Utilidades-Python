# SELECCIONAR DATOS EN DATAFRAMES

import pandas as pd
import numpy as np

matriz = np.arange(25).reshape(5, 5)

list_indices = ['i1','i2','i3','i4','i5']
list_columnas = ['c1','c2','c3','c4','c5']

# CREA DATAFRAME
dataframe = pd.DataFrame(matriz, index=list_indices, columns=list_columnas)
print(dataframe)

# ACCEDE A UNA COLUMNA DEL DATAFRAME
print(dataframe['c2'])

# ACCEDE MEDIANTE COORDENADAS A UN DATO COLUMNA:INDICE
print(dataframe['c2']['i2'])

# ACCEDE A LAS COLUMNAS PASADAS COMO UNA LISTA
print(dataframe[['c2','c4']])

# DEVUELVE VALORES BOOLEANOS, FALSE Y TRUE SEGUN CUMPLAN LA CONDICION
print(dataframe > 20)

# ACCEDE A VALORES DE UNA COLUMNA QUE CUMPLAN UNA CONDICION
print(dataframe[dataframe['c2'] > 15])

# ACCEDE A DATAFRAME MEDIANTE INDICE. CON EL METODO .LOC
print(dataframe.loc['i3'])