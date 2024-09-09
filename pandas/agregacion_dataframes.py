# Agregacion (Operaciones que dan un valor, como la media)

import numpy as np
import pandas as pd

list_valores = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.nan, np.nan]]

list_columnas = list('abc')

dataframe = pd.DataFrame(list_valores, columns=list_columnas)
print(dataframe)

# RETORNA UN DATAFRAME CON UNA FILA CON LAS SUMAS POR COLUMNA Y OTRA FILA CON EL VALOR MINIMO DE CADA COLUMNA
print(dataframe.agg(['sum', 'min']))

# RESTORNA UNA SERIE CON LAS SUMAS POR FILAS
print(dataframe.agg('sum', axis=1))
