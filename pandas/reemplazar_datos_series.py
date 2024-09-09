# REEMPLAZAR DATOS EN SERIES

import pandas as pd

print('****** SERIE1 ******')
serie1 = pd.Series([1,2,3,4,5], index=list('abcde'))
print(serie1)

print('****** SERIE2 ******')
serie2 = serie1.replace(1, 6)
print(serie2)


print('****** SERIE3 ******')
# REEMPLAZA VALORES MEDIANTE UN DICCIONARIO
serie3 = serie1.replace({2:8, 3:9})
print(serie3)