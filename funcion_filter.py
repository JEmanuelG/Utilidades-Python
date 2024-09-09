# Funcion filter

def positivo(numero):
    if numero > 0:
        return True
    else:
        return False

num_list = [2, 5 ,-6, 4, -9, -1, -3, 7, 8]

# Filter devuelve todos los valores con condicion True, como argumento se le pasa (una_funcion, arreglo_de_datos).
# Con filter no es necesario iterar sobre el arreglo
resultado = list(filter(positivo, num_list))

print(resultado)
