# arrays, matriz y matriz transpuesta
import numpy as np

# CREA UNA MATRIZ con elementos del 0 al 14 y con forma 3 filas y 5 columnas
matriz = np.arange(15).reshape((3, 5))


print(matriz)

# Crea la matriz transpuesta dejandola con forma (5, 3)
matriz_transpuesta = matriz.T
print(matriz_transpuesta)
