 # Importa modulo numpy, con np como si fuera su "apodo", de lo contrario se lo llamaría numpy dentro del script
import numpy as np

# Crea un arreglo de 4 ceros, np.numero_en_ingles(cantidad_de_numeros)
# el arreglo queda como [0.,0.,0.,0.], queda con un punto porque son float
array_zeros = np.zeros(4)
print("array_zeros =", array_zeros)

# Otro ejemplo
array_ones = np.ones(3)
print("array_ones =", array_ones)

# Crea un arreglo con un rango dado. queda como [0,1,2,3,4,5]
array_rango = np.arange(6)
print("array_rango =", array_rango)

# crea un arreglo de A a B de C en C. Queda como [2, 5, 8, 11]
array_rango_c = np.arange(2, 12, 3)
print("array_rango_c =", array_rango_c)


arreglo1 = [2,4,6]
arreglo2 = [4,5,9]

tupla = (arreglo1,arreglo2)

# Crea un arreglo con los datos de una tupla, se pueden pasar datos directamente
arreglo1y2 = np.array(tupla)

# shape devuelve la forma del array. Muestra: (2, 3)
que_shipe = arreglo1y2.shape

# dtype devuelve el tipo de dato
que_dtype = arreglo1y2.dtype

# muestra los valores que devuelve .shape y .dtype
print(que_shipe)
print(que_dtype)