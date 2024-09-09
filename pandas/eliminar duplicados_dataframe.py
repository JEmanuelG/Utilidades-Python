# ELIMINAR DUPLICADOS EN DATAFRAMES
import pandas as pd

list_valores = [[1,2],[1,2],[5,6],[5,8]]

list_indices = list('mnop')
list_columnas = ['valor1','valor2']

print("*********** DATAFRAME ***********")
dataframe = pd.DataFrame(list_valores, index=list_indices, columns=list_columnas)
print(dataframe)

print("*********** DATAFRAME2 ***********")
# ELIMINA LAS FILAS DUPLICADAS DEL DATAFRAME DEJANDO SOLO LA PRIMERA
dataframe2 = dataframe.drop_duplicates()
print(dataframe2)

print("*********** DATAFRAME3 ***********")
# ELIMINA LAS FILAS CON VALORES DUPLICADOS VASANDOSE EN LA COLUMNA VALOR1
# EN ESTE EJEMPLO LOS INDICES O Y P TIENEN EL MISMO VALOR (5), POR LO QUE SE ELIMINA LA FILA O
dataframe3 = dataframe.drop_duplicates(['valor1'])
print(dataframe3)

print("*********** DATAFRAME4 ***********")
# ELIMINA LOS DUPLICADOS QUEDANDOSE CON EL ULTIMO VALOR. KEEP='LAST'
dataframe4 = dataframe.drop_duplicates(['valor1'], keep='last')
print(dataframe4)