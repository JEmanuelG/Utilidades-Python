# FUNCINES QUE SE PUDEN APLICAR SOBRE LOS ARRAYS

import numpy as np

arreglo1 = np.arange(5)
arreglo2 = np.arange(5,10)

print(arreglo1)

# APLICA LA RAIZ 2 SOBRE EL ARRAY CON LA FUNCION .SQRT
raiz2_arreglo1 = np.sqrt(arreglo1)

print("Raiz 2 de arreglo1", raiz2_arreglo1)

# CREA UN ARREGLO DE 5 ELEMENTOS CON VALORES RANDOM
arreglo_random = np.random.rand(5)
print(arreglo_random)

# FUNCION SUMA
arreglos_suma = np.add(arreglo1, arreglo2)
print(arreglos_suma)

# FUNCION MAXIMUM.
# ARAMA UN ARREGLO CON LOS VALORES ENTRE 2 ARRAYS, COMPARANDO SEGUN INDICE
arreglo_max = np.maximum(arreglo1, arreglo2)
print(arreglo_max)