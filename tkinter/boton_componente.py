# IMPORTA MODULO TKINTER
import tkinter
from turtle import color

# CREA COMPONENTE RAIZ
raiz = tkinter.Tk()
raiz.title("Mi programa")

# CREA FUNCION QUE VA A ACCIONAR EL BOTON
# La funcion va a mostrar en consola "Hola mundo"
def accion():
    print("Hola mundo")

# CREA COMPONENTE BOTON
boton = tkinter.Button(raiz, text="Ejecutar", command=accion)


# CONFIGURA COMP BOTON
boton.config(fg="green")

# MUESTRA EL COMP EN PANTALLA
boton.pack()


# EJECUTA EL PROGRAMA
raiz.mainloop()