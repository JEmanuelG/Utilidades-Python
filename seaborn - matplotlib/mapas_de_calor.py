# Mapas de calor

import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

vuelos = sns.load_dataset('flights')
print(vuelos.head())

# CREA UNA MATRIZ CON LOS DATOS DE LA VARIABLE VUELOS
# CON MONTH COMO INDICE DE LAS FILAS Y YEAR COMO INDICES DE LAS COLUMNAS
vuelos = vuelos.pivot('month', 'year', 'passengers')
print(vuelos)

# CREA UN MAPA DE CALOR CON LOS DATOS DE LA MATRIZ
sns.heatmap(vuelos)
mpl.pyplot.show()

# AGREGA LOS VALORES EN CADA CASILLA
sns.heatmap(vuelos, annot=True, fmt='d')
mpl.pyplot.show()

# EJEMPLO DE COMO ACCEDER AL VALOR DE UN CASILLERO DE LA MATRIZ
print(vuelos.loc['May'][1956])

# ASIGAN UN DATO COMO VALOR CENTRAL DEL GRAFICO
valor_central = vuelos.loc['May'][1956]

sns.heatmap(vuelos, center=valor_central, annot=True, fmt='d')
mpl.pyplot.show()

# CAMBIA LA POSICION DE LA BARRA DE REFERENCIA, Y LA PONE HORIZONTAL
sns.heatmap(vuelos, center=valor_central, annot=True, fmt='d', cbar_kws={'orientation':'horizontal'})
mpl.pyplot.show()