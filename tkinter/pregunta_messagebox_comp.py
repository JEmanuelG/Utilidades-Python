import tkinter


from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Funcion que ejecuta el button
def preguntar():
    # retorna el valor de la respuesta del usuario
    resultado = messagebox.askquestion("Título de la pregunta", "¿Quiere borrar este fichero?")
    if (resultado == "yes"):
        print("Si, queiro boorra el fichero.")
    else:
        print("No, no quiero borrar el fichero.")


boton = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
boton.pack()

raiz.mainloop()