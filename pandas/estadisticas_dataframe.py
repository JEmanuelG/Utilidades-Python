# ESTADISTICAS EN DATAFRAMES

import numpy as np
import pandas as pd

array = np.array([[1,8,3], [5,6,7]])

dataframe = pd.DataFrame(array, index=['a', 'b'], columns=['c1', 'c2', 'c3'])

print(dataframe)

# SUMA VALORES DEL DATAFRAME POR COLUMNAS
print(dataframe.sum())

# SUMA VALORES DEL DATAFRAME POR FILAS
print(dataframe.sum(axis=1))

# DEVUELVE EL MINIMO VALOR POR COLUMNA
print(dataframe.min())

# DEVUELVE EL MINIMO VALOR POR FILA
print(dataframe.min(axis=1))

# DEVUELVE EL MAXIMO VALOR POR COLUMNA
print(dataframe.max())

# DEVUELVE EL MAXIMO VALOR POR FILA
print(dataframe.max(axis=1))

# DEVUELVE EL INDICE DEL MENOR VALOR POR COLUMNA
print(dataframe.idxmin())

# DEVUELVE EL INDICE DEL MENOR VALOR POR FILA
print(dataframe.idxmin(axis=1))

# DEVUELVE EL INDICE DEL MAYOR VALOR POR COLUMNA
print(dataframe.idxmax())

# DEVUELVE EL INDICE DEL MAYOR VALOR POR FILA
print(dataframe.idxmax(axis=1))

# DEVUELVE VALORES ESTADISTICOS DEL DATAFRAME: COUNT, MEAN, STD, MIN, 25%, 50%, 75%, MAX
print(dataframe.describe())
