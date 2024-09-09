import json

producto1 = {"nombre":"silla", "color":"blanco", "precio":80}

#convertir datos de un diccionario a una estructura JSON
estructura_json = json.dumps(producto1)

print(estructura_json)


# Convertir una estructura JSON en un diccionario
producto2 = json.loads(estructura_json)

print(producto2)
