# COMBINAR SERIES Y DATAFRAMES

import pandas as pd
import numpy as np

print("*********** SERIES ***********")

serie1 = pd.Series([1,2,np.nan])

serie2 = pd.Series([4,5,6])

# COMBINA DOS SERIES, A PARTIR DE LA SERIE1 REEMPLAZA LOS VALORES NaN CON VALORES DE LA SERIE2 SI EXISTEN
# EN ESTE EJEMPLO REEMPLAZA EL VALOR NULO DE LA FILA 2 POR EL VALOR 6
serie3 = serie1.combine_first(serie2)
print(serie3)

print("*********** DATAFRAME ***********")

list_valores = [1,2,np.nan]
dataframe1 = pd.DataFrame(list_valores)

list_valores2 = [4,5,6]
dataframe2 = pd.DataFrame(list_valores2)

# COMBINA DOS DATAFRAMES, A PARTIR DEL DATAFRAME1 REEMPLAZA LOS VALORES NaN CON VALORES DEL DATAFRAME2 SI EXISTEN
# EN ESTE EJEMPLO REEMPLAZA EL VALOR NULO DE LA FILA 2 POR EL VALOR 6
dataframe3 = dataframe1.combine_first(dataframe2)
print(dataframe3)