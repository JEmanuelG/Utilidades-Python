# ELIMINAR ELEMENTOS EN SERIES Y DATAFRAMES

import numpy as np
import pandas as pd

serie1 = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
print(serie1)

# ELIMINAR FILA DE LA SERIE
serie1 = serie1.drop('c')
print(serie1)

# CREA MATRIZ
matriz1 = np.arange(9).reshape(3, 3)

list_indices = ['a', 'b', 'c']
list_columnas = ['c1', 'c2', 'c3']

# CREA DATAFRAME
dataframe = pd.DataFrame(matriz1, index=list_indices, columns=list_columnas)
print(dataframe)

# ELIMINA FILA DE DATAFRAME
dataframe = dataframe.drop('b')
print(dataframe)

# ELIMINA COLUMNA DE DATAFRAME, SE DEBE PASA EL EJE
dataframe = dataframe.drop('c2', axis=1)
print(dataframe)