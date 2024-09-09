#IMPORTA MODULO
import tkinter

# CREA COMPONENTE RAIZ
raiz = tkinter.Tk()

# TITULA COMPONENTE RAIZ
raiz.title("Mi programa")

#CREA COMPONENTE LABEL - tkinter.Label(donde se va a mostrar el texto, text=El texto que se va a mostrar)
texto = "Hola mundo"
etiqueta = tkinter.Label(raiz, text=texto)

#CONFIGURA LA ETIQUETA
etiqueta.config(fg="green", bg="lightgrey", font=("Cortana", 30))

#MUESTRA EN PANTALLA
etiqueta.pack()

# EJECUTA PROGRAMA
raiz.mainloop()