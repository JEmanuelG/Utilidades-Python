# Regresiones lineales
# HAY QUE ACTUALIZAR, LAS FUNCIONES NO ACEPTAN PARAMETROS COMO LO MUESTRA EL CURSO

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl

# CARGA UN CONJUNTO DE DATOS QUE PROPORCIONA SEABORN PARA REALIZAR PRUEBAS
# EN ESTE EJEMPLO CARGA EL DATASET DE TIPS
propinas = sns.load_dataset('tips')

# TAMBIEN SE PUEDE ACCEDER A MAS DATOS, PASANDO COMO PARAMETRO UN VALOR A LA FUNCION: HEAD(10)
print(propinas.head())

# CREA EL GRAFICO DE LA FUNCION, TOTAL DE LAS FACTURAS EN FUNCION DE LAS PROPINAS
# SNS.LMPLOT('EJE X','EJE Y', DATASET)
sns.lmplot('total_bill', 'tip', propinas)
mpl.pyplot.show()

# MODIFICA ESTILOS DEL GRAFICO
# SCATTER_KWS PERTENECE A LOS PUNTOS
# LINE_KWS PERTENECE A LA LINEA
sns.lmplot('total_bill', 'tip', propinas, scatter_kws={'color':'green'}, line_kws={'color':'blue'})
mpl.pyplot.show()

# QUITA LA LINEA DEL GRAFICO, SOLO DEJA LOS PUNTOS
sns.lmplot('total_bill', 'tip', propinas, fit_reg=False)

# AGREGA UNA COLUMNA AL DATASET CON EL PORCENTAJE QUE REPRESENTA LA PROPINA SOBRE EL TOTAL DE LA FACTURA
propinas['porcentaje'] = 100 * propinas['tip'] / propinas['total_bill']


# CREA UN GRAFICO QUE COLOCA UN MACADOR SEGUN EL SEXO, Y ASIGNAMOS LOS TIPOS DE MARCADORES.
# GENERA DOS RECTAS, UNA PARA CADA SEXO Y ASI COMPARAR LOS VALORES SEGUN LOS SEXOS
sns.lmplot('total_bill', 'porcentaje', propinas, hue='sex', markers=['x', 'o'])
mpl.pyplot.show()

# CREA GRAFICO IDEM AL ANTERIOR PERO EN FUNCION DE LOS DIAS
sns.lmplot('total_bill', 'porcentaje', propinas, hue='day')
mpl.pyplot.show()