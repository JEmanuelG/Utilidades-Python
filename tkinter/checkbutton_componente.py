import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Funcion que ejecuta el checkbutton
def verificar():
    valor = check1.get()
    if (valor == 1):
        print("El check está activado.")
    else:
        print("El check está desactivado.")

# Variable del check button
check1 = tkinter.IntVar()

boton = tkinter.Checkbutton(raiz, text="Opción 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
boton.pack()

raiz.mainloop()