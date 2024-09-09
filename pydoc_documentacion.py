
# pydoc - Generar documentacion

#Con pydoc se puede generar documentación automaticamente desde la terminal de comandos

class Saludos:
    '''
    Esta es la documentación de la clse saludos
    Tendrá dos funciones buenos_dias y adios
    y ambas será necesario pasarle un parametro con el nombre de una persona
    '''

    def buenos_dias(self, nombre):
        ''' Esta función sirve para darle los buenos días a una persona pasando el nombre como parametro '''
        print("Buenos días, {}.".format(nombre))

    def adios(self, nombre):
        ''' Esta función sirve para decirle adiós a una persona pasando el nombre como parametro '''
        print("Adiós, ".format(nombre))

    # Ejecutamos el archivo.py desde la consola
    #ejecutamos el comando: pydoc ././archivo.py (La ruta del archivo). Y retorna la documentacion del archivo
    # Con el comando pydoc -w .././archivo.py, crea un HTML con la documentacion