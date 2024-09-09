
# Docstrings - Cadenas para documentacón

def saludar(nombre):
    # Dentro de tres pares de comillas simples o dobles ponemos un breve descripcion del proposito de la funcion
    '''
    Esto será un comentario de la función saludar.
    Esta función recibirá como parametro una cadena con el nombre e 
    imprimirá por consola un saludo con el nombre concatenado
    '''
    print("Buenos días "+ nombre)

class Saludos:
    # Al igual que en la funcion se puede aplicar en clases
    '''
    Esta clase tendrá dos funciones buenos:dias y adios
    Ambas funciones recibirán como parametro un nombre
    '''

    def buenos_dias(self, nombre):
        '''Esta función sirve para decir buenos días a una persona.'''
        print("Buenos días {}".format(nombre))

    def adios(self, nombre):
        '''Esta función sirve para decir adiós a una persona.'''
        print("Adiós {}".format(nombre))


# Con help obtenemos la documentacion antes mencionada
help(saludar)

help(Saludos)
