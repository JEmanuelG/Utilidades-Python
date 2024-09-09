# IMPORTA MODULO
import tkinter

# CREA COMPONENTE RAIZ
raiz = tkinter.Tk()

# TITULA COMPONENTE RAIZ
raiz.title("Mi programa")

# CREA COMPONENTE ENTRY
entrada = tkinter.Entry(raiz)
entrada_contraseña = tkinter.Entry(raiz)

#CONFIGURA COMPONENTE ENTRY
# justify=center centra el campo de entrada, show= es de la manera que se va a mostrar el campo
entrada.config(justify="center")
# en este campo se muestran solo * como si fuera una contraseña
entrada_contraseña.config(justify="center", show="*")

# MUESTRA POR PANTALLA
entrada.pack()
entrada_contraseña.pack()

# EJECUTA PROGRAMA
raiz.mainloop()