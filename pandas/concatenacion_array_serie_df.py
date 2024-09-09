# CONCATENECION DE ARRAYS, SERIES Y DATAFRAMES

import pandas as pd
import numpy as np

print("*************** ARRAYS ***************")

array1 = np.arange(9).reshape(3,3)
print(array1)

# CONCATENA UN ARRAY DOS VECES
array2 = np.concatenate([array1,array1])
print(array2)

# CONCATENA UN ARRAY DOS VECES SOBRE LA MISMA FILA
array2 = np.concatenate([array1,array1], axis=1)
print(array2)

print("*************** SERIES ***************")

serie1 = pd.Series([1,2,3], index=['a','b','c'])
serie2 = pd.Series([4,5,6], index=['d','e','f'])

# CONCATENA DOS SERIES, UNA DEBAJO DE LA OTRA
serie3 = pd.concat([serie1, serie2])
print(serie3)

# CONCATENA DOS SERIES, UNA DEBAJO DE LA OTRA, CON KEYS QUE IDENTIFICAN A QUE SERIE PERTENECEN LOS VALORES
# LAS KEYS VAN POR ORDEN DE CARGA
serie3 = pd.concat([serie1, serie2], keys=['serie1', 'serie2'])
print(serie3)

print("*************** DATAFRAME ***************")

dataframe1 = pd.DataFrame(np.random.rand(3,3), columns=['a','b','c'])

dataframe2 = pd.DataFrame(np.random.rand(2,3), columns=['a','b','c'])

# CONCATENA DOS DATAFRAMES
dataframe3 = pd.concat([dataframe1, dataframe2])
print(dataframe3)

# CONCATENA DOS DATAFRAMES, INGNORANDO LOS INDICES ORIGINALES
# Y LES PONE INDICES SEGUN CORRESPONDE A LA CANTIDAD DE FILAS
dataframe3 = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframe3)