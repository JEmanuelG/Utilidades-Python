# INDICES EN SERIES Y DATAFRAMES

# IMPORTA MODULO PANDAS
import pandas as pd

list_valores = [1,2,3]
list_indices = ['a', 'b', 'c']

# CREA UNA SERIE
serie = pd.Series(list_valores, index=list_indices)
print(serie)

# RETORNA UNA LISTA CON LOS INDICES
print(serie.index)

# PARA ACCEDER AL INDICE, RETORNA 'a'. NO SE PUEDEN MODIFICAR LOS DATOS DE LOS INDICES, 
# EN CAMBIO LOS VALORES SI PUEDEN SER CAMBIADOS
print(serie.index[0])

# CREA LISTAS PARA EL EJEMPLO
list_notas = [[6,7,8],[8,9,5],[6,9,7]]
list_indices = ['matematicas', 'historia', 'fisica']
list_nombres = ['Antonio', 'Maria', 'Pedro']

# CREA DATAFRAME A PARTIR DE 3 LISTAS
dataframe_notas = pd.DataFrame(list_notas, index=list_indices, columns=list_nombres)
print(dataframe_notas)
