
# Map _ Sirve para aplicar una funcion a una lista

def multiplicar_x_dos(numero):
    return numero * 2

list_num = [4, 3 , 8]

mapeo = map(multiplicar_x_dos, list_num)

resultado = list(mapeo)
print(resultado)

# DE OTRA MANERA MAS SIMPLE
resultado = list(map(multiplicar_x_dos, list_num))
print(resultado)

# DE OTRA MANERA CON LAMBDA
resultado = list(map(lambda numero: numero * 2, list_num))
print(resultado)