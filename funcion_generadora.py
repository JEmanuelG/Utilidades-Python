# range una funcion generadora

def pares(maximo):
    ''' Esta funcion va retornando los números pares dentro del rango 0 y el numero pasado por parametro '''

    for numero in range(maximo):
        if (numero % 2 == 0):
# yield retorna valores parcialmente, o sea, no es necesario que termine el script de la funcion para que retorne valores            
            yield numero

max = 11
for n in pares(max):
    print(n)