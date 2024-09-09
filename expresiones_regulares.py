#Importar el modulo de expresiones regulares
import re

#Search
print("********** SEARCH **********")

texto = "Hola, me llamo Emanuel, chau."

# search busca algo dentro de una variable y retorna un bool
busqueda = re.search("Emanuel", texto)

if busqueda:
    print("encontrado")
    # de esta manera podemos saber la posicion en la que se encuentra la palabra que buscamos
    inicial = busqueda.start()
    final = busqueda.end()
    print("Empieza en la posición {} y termina en la {} del texto.".format(inicial, final))
else:
    print("no encontrado")

# Con el signo $ al final, pregunta si hay alguna frase que termine con esa palabra
re.search("Emanuel$", texto)

# Con el signo ^ al final, pregunta si hay alguna frase que empiece con esa palabra
busqueda = re.search("^Hola", texto)

if busqueda:
    print("encontrado")
else:
    print("no encontrado")

#con un . y un * se pueden buscar frases dando la palabra inicial y final aunque tengan caracteres en medio
#con el . decimos que puede haber cualquier tipo de caracter y con * que puede haber 0 o mas caracteres
busqueda = re.search("me.*chau", texto)

if busqueda:
    print("encontrado")
else:
    print("no encontrado")


# FINDALL
print("********** FINDALL **********")

texto2 = """El auto de Luis es rojo,
el auto de Antonio es blanco,
y el auto de María es rojo"""

#findall funciona similar al ejemplo anterior pero devuelve una lista con las coincidencias
busqueda2 = re.findall("auto.*rojo", texto2)

print(busqueda2)


# SPLIT
print("********** SPLIT **********")

texto3 = "La silla es blanca y vale 80"

# Dado un parametro divide el texto y va almacenando los fragmentos en una lista sin incluir el parametro.
# \s es un espacio
busqueda3 = re.split("\s", texto3)

print(busqueda3)


# SUB
print("********** SUB **********")

texto4 = "La silla es blanca y vale 80"

# Sustituye el paramtro que le demos por otro
busqueda4 = re.sub("blanca", "roja", texto4)

print(busqueda4)