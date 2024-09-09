# JERARQUIA EN LOS INDICES DE SERIES Y DATAFRAMES

import pandas as pd
import numpy as np

list_valores = np.random.rand(6)

# CREA SERIE CON DOBLE INDICE, NOTE QUE HAY UN INDICE PRINCIPAL PARA CADA SUBINDICE
# 1,1,1 PARA a,b,c, Y 2,2,2 para a,b,c
list_indices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]

serie = pd.Series(list_valores, index=list_indices)
print(serie)

# MUESTRA TODO EL CONTENIDO DEL INDICE 1
print(serie[1])

# MUESTRA EL CONTENIDO DEL INDICE 1 SUBINDICE b
print(serie[1]['b'])

# CREA DATAFRAME A PARTIR DE UNA SERIE
dataframe = serie.unstack()
print(dataframe)


# CREA DATA FRAME PARA EJEMPLO
list_valores2 = np.arange(16).reshape(4,4)

list_indices2 = list('1234')
list_columnas2 = list('abcd')

dataframe2 = pd.DataFrame(list_valores2, index=list_indices2, columns=list_columnas2)
print(dataframe2)

# CREA SERIE A PARTIR DE DATAFRAME, CON INDICE PRINICIPAL LAS FILAS Y SUBINDICE LAS COLUMNAS(CON UNSTACK LOS HACE AL REVÉS, COLUMNAS/FILAS)
serie = dataframe2.stack()
print(serie)