# HISTOGRAMAS

import numpy as np
import pandas as pd

import matplotlib as mpl
import seaborn as sns

# ESTA LINEA PERMITE VER LOS GRAFICOS DE LOS EJEMPLOS EN JUPYTER (NO FUNCIONA)
#%matplotlib

# CREA ARRAY CON 100 VALORES ALEATORIOS +/-
datos1 = np.random.randn(100)

datos2 = np.random.randn(80)

# CREA UN HISTOGRAMA CON MATPLOTLIB CON LOS DATOS DE UN ARREGLO
# ALPHA DEFINE LA INTENCIDAD DEL COLOR DE LAS BARRAS DEL HISTOGRAMA
mpl.pyplot.hist(datos1, color='green', alpha=0.8)

# VISUALIZA EL GRAFICO EN UNA VENTANA
mpl.pyplot.show()

# IDEM A MATPLOTLIB PERO CON SEABORN
sns.distplot(datos1, color='blue')

mpl.pyplot.show()

# CREA UN HISTOGRAMA COMBINANDO 2 HISTOGRAMAS
# BINS - DECLARAMOS LA CANTIDAD DE COLUMNAS QUE QUEREMOS EN EL GRAFICO
# DENSITY - AL PONERLO EN TRUE, PASA POR ALTO QUE LA CANTIDAD DE VALORES ENTRE ARREGLOS NO COINCIDAN 
mpl.pyplot.hist(datos1, color='green', alpha=0.5, bins=20, density=True)
mpl.pyplot.hist(datos2, color='blue', alpha=0.5, bins=20, density=True)

mpl.pyplot.show()

# IDEM QUE MATPLOTLIB PERO CON SEABORN
# CREA UN GRAFICO CON PUNTOS DE COINCIDENCIA (NO FUNCIONA PASANDO 2 PARAMETROS COMO EN EL CURSO)
sns.jointplot(datos1)

mpl.pyplot.show()

# KIND - LE DA DISTINTAS FORMAS A LOS PUNTOS, EN ESTE CASO POLIGONOS HEXAGONOS (NO FUNCIONA PASANDO 2 PARAMETROS COMO EN EL CURSO)
sns.jointplot(datos1, kind='hex')

mpl.pyplot.show()