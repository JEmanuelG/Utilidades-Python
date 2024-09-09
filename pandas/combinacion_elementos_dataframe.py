# COMBINACIONES DE ELEMENTOS EN DATAFRAMES
import pandas as pd
import numpy as np

list_valores = np.arange(25).reshape(5,5)

dataframe = pd.DataFrame(list_valores)
print(dataframe)

# GENERA UN ARREGLO CON 5 VALORES DEL 0 AL 4 CON UN ORDEN ALEATORIO
valores_aleatorios = np.random.permutation(5)
print(valores_aleatorios)

# ORDENA LAS FILAS SEGUN EL ARREGLO PASADO POR PARAMETRO
dataframe = dataframe.take(valores_aleatorios)
print(dataframe)