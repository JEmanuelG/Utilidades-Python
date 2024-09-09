# AGRUPAR DATOS EN CATEGORIAS

import pandas as pd
import numpy as np

precios = [42,55,48,23,5,21,88,34,26]
rango = np.arange(0, 101, 10)

# AGRUPA PRECIOS DENTRO DE LOS RANGOS
precio_con_rango = pd.cut(precios, rango)
print(precio_con_rango)

# RETORNA UNA SERIE CON LOS RANGOS Y LA CANTIDAD DE VALORES QUE PERTENECES A CADA RANGO
cantidad_x_categoria = pd.value_counts(precio_con_rango)
print(cantidad_x_categoria)