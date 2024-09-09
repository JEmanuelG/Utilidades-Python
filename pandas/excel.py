# FICHEROS EN FORMATO EXCEL

import pandas as pd

# LEE EL FICHERO EXCEL
fichero_excel = pd.ExcelFile('C:/Users/Emanuel/Desktop/Cursos/Python/Python/campeones del mundo.xlsx')

# LEE FICHERO CSV, QUE ES SIMILAR A EXCEL. Y DE ESTA MANERA YA QUEDA COMO UN DATAFRAME
file_csv = pd.read_csv('C:/Users/Emanuel/Desktop/Cursos/Python/otros ejercicios/seccion21/poblacion.csv')

# CREA DATAFRAME CON LOS DATOS DE LA "Hoja1"
dataframe = fichero_excel.parse('Hoja1')
print(dataframe)