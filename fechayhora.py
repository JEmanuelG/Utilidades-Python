from datetime import datetime

# guardamos los datos en una variable
fechayhora = datetime.now()

print(fechayhora)

#accedemos a los datos guaradados en la variable fechayhora
anio = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day
hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

print("La hora es: {}:{}:{}".format(hora, minutos, segundos))

