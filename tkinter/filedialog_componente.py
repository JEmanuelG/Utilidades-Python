import tkinter

from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi programa")

def abrir_fichero():
    # Nos da la opcion de seleccionar un fichero y retorna su ruta
    ruta_fichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(ruta_fichero)

boton = tkinter.Button(raiz, text="Pulsar para empezar", command=abrir_fichero)
boton.pack()

raiz.mainloop()