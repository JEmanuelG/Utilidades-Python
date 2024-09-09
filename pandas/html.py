
import pandas as pd

url ='https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

# LEE LOS DATOS DEL HTML DE LA URL Y CREA DATAFRAME
dataframe = pd.io.html.read_html(url)
print(dataframe)

# CREA DATAFRAME QUE NOS INTERESA, SOLO CON LOS DATOS DE LA POSICION 0, LA TABLA DE CAMPEONES DEL MUNDO
dataframe_futbol = dataframe[0]
print("\nDATAFRAME_FUTBOL\n")
print(dataframe_futbol)


# DE ESTA MANERA RENOMBRA LAS COLUMNAS CON LOS NOMBRES DE LA FILA 0, EN ESTE CASO NO APLICA PORQUE SE RECUPERO
# LOS DATOS DEL HTML CON LAS COLUMNAS BIEN NOMBRADAS, PERO PUEDE PASAR QUE LAS COLUMNAS ESTEN NOMBRADAS CON
# NUMERO Y SUS NOMBRES ESTEN UBICADOS EN LA PRIMER FILA

dataframe_futbol = dataframe_futbol.rename(columns=dict(dataframe_futbol.loc[0]))

# ELIMINA LA PRIMER FILA QUE SE SUPONE QUE ESTARIAN LOS NOMBRES DE LAS COLUMNAS, AL RENOMBRAR LA COLUMNAS
# CORRECTAMENTE, ESTA FILA QUEDARIA DEMAS

dataframe_futbol = dataframe_futbol.drop(0)

# ELIMINA COLUMNA 'NOTAS', NOTE QUE SE PASA COMO SEGUNDO PARAMETRO AXIS=1 PARA DECIRLE QUE ESTA
# EN COLUMNAS Y NO FILAS
dataframe_futbol = dataframe_futbol.drop('Notas', axis=1)
print(dataframe_futbol)