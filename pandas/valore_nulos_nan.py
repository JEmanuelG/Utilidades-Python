
# VALORES NULOS EN SERIES Y DATAFRAMES

import pandas as pd
import numpy as np

list_valores = [1,2, np.nan, 4]

serie = pd.Series(list_valores, index=list('abcd'))
print(serie)

# RETORNA VALORES BOOL DEPENDIENDO DE SI LOS VALORES NULOS O NO
print(serie.isnull())

# ELIMINA LOS VALORES NULOS DE LA SERIE JUNTO CON SU INDICE Y FILA
serie = serie.dropna()
print(serie)

# DATAFRAMES

list_valores = [[1,2,3],[4,np.nan, 5],[6, 7, np.nan]]
list_indices = list('123')
list_columnas = ['c1', 'c2', 'c3']


dataframe = pd.DataFrame(list_valores, index=list_indices, columns=list_columnas)
print(dataframe)

# RETORNA VALORES BOOL DEPENDIENDO SI LOS VALORES SON NULOS O NO
print(dataframe.isnull())

# ELIMINA LOS VALORES NULOS DE LA SERIE JUNTO CON SU INDICE Y FILA
dataframe = dataframe.dropna()
print(dataframe)

dataframe = pd.DataFrame(list_valores, index=list_indices, columns=list_columnas)
print(dataframe)

# ASIGNA UN VALOR X A LOS VALORES NULOS 
dataframe = dataframe.fillna(0)
print(dataframe)
