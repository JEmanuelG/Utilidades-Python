# AGRUPACION EN DATAFRAMES

import pandas as pd
import numpy as np

list_valores = {'clave1':list('xxyyz'), 'clave2':list('ababa'),
                'datos1':np.random.rand(5), 'datos2':np.random.rand(5)}

dataframe = pd.DataFrame(list_valores)
print(dataframe)

# CREA UNA VARIABLE CON LOS DATOS DE UN GRUPO PASADO POR PARAMETROS
# TOMA LOS DATOS DE LA COLUMNA 'datos1' Y LOS AGRUPA SEGUN LA COLUMNA 'clave1' PARA LUEGO PODER OPERAR CON ELLOS
grupo1 = dataframe['datos1'].groupby(dataframe['clave1'])


# CALCULA LA MEDIA DE LOS VALORES POR CADA CLAVE
print(grupo1.mean())