# Union de dataframes

from sqlite3 import DatabaseError
import pandas as pd

# CREA DATAFRAMES A PARTIR DE DICCIONARIOS
dataframe1 = pd.DataFrame({'c1': ['1','2','3'], 'clave': ['a','b','c']})

dataframe2 = pd.DataFrame({'c2': ['4','5','6'], 'clave': ['c','b','e']})

# CREA UN DATAFRAME CON LA UNION DE 2 DATAFRAMES,
# O SEA, CON LOS ELEMENTOS QUE TIENEN EN COMUN LOS DATAFRAMES DADOS SEGUN LA COLUMNA "CLAVE"
# CON ON= LE PASAMOS LA COLUMNA CON LA QUE QUEREMOS QUE HAGA LA UNION
dataframe3 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave')
print(dataframe3)

# CON EL PARAMETRO HOW= LE DECIMOS QUE DATAFRAME PONER DIRECTAMENTE
# PARA LUEGO AGREGAR SOBRE ESE DF LOS ELEMENTOS EN COMUN CON LOS OTROS DF. 
# Y LOS CAMPOS QUE NO TIENEN COINCIDENCIAS LOS DEJA CON VALOR NaN 
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='left')
print(dataframe4)


# HACE LO MISMO QUE EL ANTERIOR PERO LE DECIMOS QUE PREVALEZCA EL DATAFRAME 2
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='right')
print(dataframe4)

# CON HOW='OUTER' UNIMOS LOS DATAFRAMES CON TODOS SUS DATOS, Y PONE VALOR NULO DONDE NO HAY COINCIDENCIAS
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='outer')
print(dataframe4)