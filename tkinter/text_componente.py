# IMPORTA MODULO
import tkinter

# CREA COMPONENTE RAIZ
raiz = tkinter.Tk()
raiz.title("Mi programa")

# CREA COMPONENTE DE ENTRADA DE TEXTO
entrada = tkinter.Text(raiz)

# CONFIGURA EL COMP DE ENTRADA DE TEXTO
entrada.config(width=20, height=10, font=("Verdana",15), padx=10, pady=10, fg="green", selectbackground="lightgrey")

# MUESTRA EN PANTALLA EL COMP ENTRADA
entrada.pack()
# EJECUTA EL PROGRAMA
raiz.mainloop()