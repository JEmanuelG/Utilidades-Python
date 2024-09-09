# OREDENAR Y CLASIFICAR SERIES

import pandas as pd
import numpy as np

list_valores = np.arange(4)
list_indices = list('CABD')

serie = pd.Series(list_valores, index=list_indices)
print(serie)

# OREDENA SERIE POR LOS INDICES
serie = serie.sort_index()
print(serie)

# ORDENA LA SERIE POR LOS VALORES, DE MENOR A MAYOR
serie = serie.sort_values()
print(serie)

# CREA UNA SERIE CON VALORES RANDOM
serie2 = pd.Series(np.random.randn(10))
print(serie2)

# RETORNA EL RANKING QUE OCUPA CADA VALOR DE MENOR A MAYOR, O SEA, EL MENOR VALOR ESTA EN LA POSICION 1
print(serie2.rank())