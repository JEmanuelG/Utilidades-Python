# DIAGRAMA DE CAJA
# Sirve para representar graficamente una serie de datos numéricos a través de sus cuartos,
# mostrando el rango a donde pertenece el 50% de los valores y el 25% hacia la izquierda y derecha

import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

datos = np.random.randn(100)

# CREA GRAFICO DE DIAGRAMA DE CAJA
sns.boxplot(datos)
mpl.pyplot.show()