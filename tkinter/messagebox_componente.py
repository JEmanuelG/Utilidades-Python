import tkinter

# DEBE LLAMAR A MESSAGEBOX ESPECIFICAMENTE PARA SU CORRECTO FUNCIONAMIENTO
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
    messagebox.showinfo("Título", "Mensaje con la información")

boton1 = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton1.pack()

raiz.mainloop()