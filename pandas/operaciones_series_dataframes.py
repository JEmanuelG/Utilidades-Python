# OPERACIONES SOBRE SERIES Y DATAFRAMES

import pandas as pd
import numpy as np

serie1 = pd.Series(list('012'), index=list('abc'))

serie2 = pd.Series(list('3456'), index=list('abcd'))

# SUMA DOS SERIES
serie3 = serie1 + serie2
print(serie3)

# CREA MATRIZ CON NUMPY
list_valores = np.arange(4).reshape(2,2)
list_indices = list('ab')
list_columnas = list('12')

list_valores2 = np.arange(9).reshape(3,3)
list_indices2 = list('abc')
list_columnas2 = list('123')

# CREA DATAFRAME
dataframe = pd.DataFrame(list_valores, index=list_indices, columns=list_columnas)
print(dataframe)

dataframe2 = pd.DataFrame(list_valores2, index=list_indices2, columns=list_columnas2)
print(dataframe2)

# SUMA DOS DATAFRAME
# DE ESTA MANERA QUEDAN CASILLAS NaN PORQUE NO TIENEN LA MISMA CANTIDAD DE FILAS Y COLUMNAS
dataframe3 = dataframe + dataframe2
print(dataframe3)

# LA MANERA CORRECTA ES USANDO ADD Y ASIGNANDO EL VALOR 0 A LOS VALORES QUE NO EXISTEN CON FILL_VALUE=0
dataframe3 = dataframe.add(dataframe2, fill_value=0)
print(dataframe3)
