# SELECCIONAR DATOS EN LAS SERIES

import pandas as pd
import numpy as np

list_valores = np.arange(3)
list_indices = ['i1', 'i2', 'i3']

# CREA UNA SERIE
serie = pd.Series(list_valores, index=list_indices)
print(serie)

# APLICA OPERADORES MATEMATICOS SOBRE LA SERIE
serie *= 2
print(serie)

# ACCEDE MEDIANTE INDICE ESTABLECIDO
print(serie['i2'])

# ACCEDE MEDIANTE POSICION
print(serie[1])

# ACCEDE MEDIANTE POSICION DESDE HASTA
print(serie[0:3])

# ACCEDE MEDIANTE INDICE ESTABLECIDO DESDE HASTA
print(serie['i1':'i3'])

# ACCEDE A LOS INDICES QUE PONEMOS DENTRO DE LOS CORCHETES COMO UNA LISTA
print(serie[['i1','i3']])

# ACCEDER A DATOS SEGUN CONDICION
print(serie[serie > 3])

# MODIFICA EL VALOR DE LOS DATOS QUE CUMPLEN LA CONDICION
serie[serie > 3] = 6
print(serie)