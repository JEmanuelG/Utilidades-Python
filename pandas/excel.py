# FICHEROS EN FORMATO EXCEL

import pandas as pd

# LEE EL FICHERO EXCEL
fichero_excel = pd.ExcelFile('C:/Users/Emanuel/Desktop/Python/campeones del mundo.xlsx') # Acá va la dirección de la ubicación del archivo

# LEE FICHERO CSV, QUE ES SIMILAR A EXCEL. Y DE ESTA MANERA YA QUEDA COMO UN DATAFRAME
file_csv = pd.read_csv('C:/Users/Emanuel/Desktop/Python/otros ejercicios/seccion21/poblacion.csv') # Acá va la dirección de la ubicación del archivo

# CREA DATAFRAME CON LOS DATOS DE LA "Hoja1"
dataframe = fichero_excel.parse('Hoja1')
print(dataframe)
