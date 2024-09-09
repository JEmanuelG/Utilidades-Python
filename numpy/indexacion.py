# Indexacion con numpy

import numpy as np

array1 = np.arange(11)
print("array1 =", array1)

# Crea un sub arreglo de array1
array_corto = array1[:3]
print("array_corto de del 0 al 2 =", array_corto)

# Crea una copia de array1
array_copia = array1.copy()

# Modifica los elementos con indice 0,1 y 2 y los deja en 20
array_copia [0:3] = 20

# Acceder a un array de mas de una dimension array[fila][columna]

