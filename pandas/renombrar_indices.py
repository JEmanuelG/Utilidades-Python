# RENOMBRAR INDICES

import pandas as pd
import numpy as np

list_valores = np.arange(9).reshape(3,3)

list_indices = list('abc')

dataframe = pd.DataFrame(list_valores, index=list_indices)
print(dataframe)

print('***** 1ER EJEMPLO *****')

# TOMA LOS INDICES DEL DATAFRAME Y LOS GUARDA EN MAYUSCULAS EN UNA VARIABLE
nuevos_indices = dataframe.index.map(str.upper)

# ASIGNA LOS INDICES DE UNA VARIABLE AL DATAFRAME
dataframe.index = nuevos_indices
print(dataframe)

print('***** 2DO EJEMPLO *****')
# RENOMBRA LOS INDICES DEL DATAFRAME Y LOS PONE EN MINUSCULAS
dataframe = dataframe.rename(index=str.lower)
print(dataframe)

print('***** 3ER EJEMPLO *****')
nuevos_indices = {'a':'f', 'b':'g', 'c':'h'}
# RENOMBRA LOS INDICES DEL DATAFRAME MEDIANTE UN DICCIONARIO
dataframe = dataframe.rename(index=nuevos_indices)
print(dataframe)

print('***** 4TO EJEMPLO *****')
nuevos_indices = {'f':'j'}

# RENOMBRA LOS INDICES DEL DATAFRAME MEDIANTE UN DICCIONARIO
# USA METODO INPLACE=TRUE PARA HACER EFECTIVO EL CAMBIO, SIN NECESCIDAD DE USAR DF=DF.RENAME()
dataframe.rename(index=nuevos_indices, inplace=True)
print(dataframe)