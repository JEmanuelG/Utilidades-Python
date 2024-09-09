import modulo1 # importa el modulo completo
from modulo1 import funcion # importa una funcion en especifico
from modulo1 import funcion as mifuncion # importa una funcion en especifico y la guarde como "mifuncion"

conjunto = {"rojo", "azul", "amarillo"}

diccionario = {"red":"rojo", "blue":"azul", "yellow":"amarillo"}

print(diccionario)

diccionario["black"] = "negro"

print(diccionario)

diccionario.pop("red")

print(diccionario)

for clave, valor in diccionario.items():
    print(clave, valor)


# lamda, en una sola linea puede crea la funcion "promedio(n1,n2,n3)" que retorna el promedio de esos parametros
promedio = lambda n1, n2, n3 : (n1 + n2 + n3) / 3