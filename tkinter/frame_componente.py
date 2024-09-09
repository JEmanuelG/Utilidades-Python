# IMPORTA MODULO
import tkinter

# CREA COMPONENTE RAIZ
raiz = tkinter.Tk()
# TITULA COMPONENTE RAIZ
raiz.title("Mi programa")

#CREA COMPONENTE FRAME
frame = tkinter.Frame(raiz)

# CONFIGURA COMP FRAME
frame.config(bg="blue", width=400, height=300)

# MUESTRA COMPONENTE FRAME EN PANTALLA
frame.pack()

# EJECUTA EL PROGRAMA
raiz.mainloop()