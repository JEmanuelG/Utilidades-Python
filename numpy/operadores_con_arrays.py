# Operadores matemáticos con arrays (+, -, *, /, **)

import numpy as np

array1 = np.array([1,2,3,4,5])
print("Array1 ariginal =", array1)

# Con numpy el arreglo puede manipularse con mas facilidad
# Puede utilizarse con cualquier operador
array1 += 4
print("Array1 + 4 =", array1)

# Otro ejemplo, eleva al cuadrado cada elemento del arreglo
array1 **= 2
print("Array1 ** 2 =", array1)

lista1 = [1,2,3]
lista2 = [4,5,6]

array_doble = np.array([lista1, lista2])

print("array_doble original =", array_doble)

# Los operadores tambien se pueden utilizar sobre arreglos de mas de una dimension
array_doble **= 2
print("array_doble ** 2 =", array_doble)