# FILTRAR DATOS EN DATAFRAMES

import pandas as pd
import numpy as np

# CREA UN ARRAY DE 10 ELEMENTOS CON 3 VALORES RANDOM, O SEA 10FILAS Y 3 COLUMNAS
list_valores = np.random.rand(10, 3)

dataframe = pd.DataFrame(list_valores)
print(dataframe)


print('\nCOLUMNA 0 DEL DATAFRAME\n')
# GUARDA LOS DATOS DE LA COLUMNA 0 EN UNA VARIABLE
columna = dataframe[0]
print(columna)

# FILTRA SOLO LOS VALORES QUECUMPLEN LA CONDICION, EL RESTO NO LOS MUESTRA
print(columna[columna > 0.40])

# FILTRA SOLO LOS VALORES QUECUMPLEN LA CONDICION, LOS QUE NO QUEDAN COMO NULOS
print(dataframe[dataframe > 0.40])