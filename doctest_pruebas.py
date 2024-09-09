
# Doctest - Generar pruebas dentro de la documentacion

def sumar(numero1, numero2):
    '''
    Esto es la documentación de esta función.
    Recibe dos numeros como parametros y retorna la suma de ellos

    >>> sumar(4, 3)
    7

    >>> sumar(8, 4)
    12

    >>> sumar(5, 5)
    10
    '''  
#Se le pasan las lineas a ejecutar dentro de la cadena de la cadena de la documentacion con el respectivo
# valor como resultado. >>> funcion(parametros) y en la sig valor que debería retornar
    return numero1 + numero2


resultado = sumar(3, 5)
print(resultado)


# Esto permite que se ejecute la prueba
import doctest
doctest.testmod()

# el comando para ejecutarlo en consola. con -v da la orden de verificar las pruebas que pusimos dentro de la doc
# python archivo.py -v
