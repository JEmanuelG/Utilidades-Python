#COMBINANDO ESTILOS

import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns


# CREA UN ARREGLO CON 100 VALORES ALEATORIOS
datos1 = np.random.randn(100)

# MUESTRA EL GRAFICO DEL ARREGLO
sns.distplot(datos1)
mpl.pyplot.show()

# MUESTRA SOLO LA CURVA DEL GRAFICO, PONIENDO LOS PARAMETROS EN FALSE
sns.distplot(datos1, color="green", rug=False, hist=False)
mpl.pyplot.show()

# CREA VARIABLES CON ARGUMENTOS PARA PASARLE A LA FUNCION DISTPLOT
argumentos_curva = {'color':'black', 'label':'Curva'}
argumentos_histograma = {'color':'grey', 'label':'Histograma'}

# LOS PARAMETROS KDE_KWS PERTENECEN A LA CURVA
# LOS PARAMETROS HIST_KWS PERTENECEN AL HISTOGRAMA
sns.distplot(datos1, bins=25, kde_kws=argumentos_curva, hist_kws=argumentos_histograma)
mpl.pyplot.show()

# CREA UN GRAFICO A PARTIR DE UNA SERIE
serie1 = pd.Series(datos1)
sns.distplot(serie1, bins=25, color='red')
mpl.pyplot.show()