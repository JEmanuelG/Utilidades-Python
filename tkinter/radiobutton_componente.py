# IMPORTA MODULO TKINTER
import tkinter

# CREA COMPONENTE RAIZ
raiz = tkinter.Tk()
raiz.title("Mi programa")

# DEFINE LA FUNCION QUE ACCIONAN LOS RADIOBUTTONS
# el get() toma el valor que se le asigna a la variable opcion al momento de ejecutarlo
def seleccionar():
    print("La opción seleccionada es {}".format(opcion.get()))

# CREA VARIABLE UTILIZADA EN EL COMPONENTE
opcion = tkinter.IntVar()

# CREA COMPONENTES RADIOBUTTON
botonradio1 = tkinter.Radiobutton(raiz, text="Opción 1", variable=opcion, value=1, command=seleccionar)
# MUESTRA EN PANTALLA
botonradio1.pack()

botonradio2 = tkinter.Radiobutton(raiz, text="Opción 2", variable=opcion, value=2, command=seleccionar)
botonradio2.pack()

botonradio3 = tkinter.Radiobutton(raiz, text="Opción 3", variable=opcion, value=3, command=seleccionar)
botonradio3.pack()


# EJECUTA EL PROGRAMA
raiz.mainloop()