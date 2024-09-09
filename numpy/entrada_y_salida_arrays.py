# Entrada y salida de arrays

import numpy as np

arreglo1 = np.arange(6)

# GUARDA EL ARRAY arreglo1 CON EL NOMBRE arreglos1save
np.save('arreglo1save', arreglo1)

# CARGA EL ARRAY, SE DEBE PONER LA EXTENCION DEL ARCHIVO .NPY
arreglo_cargado = np.load('arreglo1save.npy')
print(arreglo_cargado)

arreglo2 = np.arange(6,10)

# GUARDA DOS ARRAYS CON EL NOMBRE arreglossavez. (.savez)
# PASANDOLE EN LAS COORDENADAS X E Y LOS ARRAYS

np.savez('arreglossavez', x=arreglo1, y=arreglo2)

# CARGA LOS ARRAYS EN UNA VARIABLE, SE DEBE PONER LA EXTENCION DEL ARCHIVO .NPZ
arreglos_cargados_2d = np.load('arreglossavez.npz')

# RECUPERA LOS ARRAYS PASANDO INDEX DE LA VARIABLE
print(arreglos_cargados_2d['x'])
print(arreglos_cargados_2d['y'])

# GUARDA ARRAY EN FICHERO TXT (.savetxt)
# delimiter ES COMO VA A QUEDAR GUARDADO LIMITADOR QUE SEPARA LOS ELEMENTOS DEL ARRAY
np.savetxt('ficheroarray.txt', arreglo1, delimiter=',')

#CARGA EL FICHERO (.loadtxt)
arreglo_cargado_txt = np.loadtxt('ficheroarray.txt')
print(arreglo_cargado_txt)