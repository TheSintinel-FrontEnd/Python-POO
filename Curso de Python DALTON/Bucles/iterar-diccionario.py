#Creamos un diccionario
diccionario = {
    
    "Nombre" : "Alfredo",
    "Apellido" : "Patiño",
    "edad" : 20
}

# Imrpimimos el diccionario
# print (diccionario) 

# Recorriendo diccionario con item() para obtener la clave y el valor 

for datos in diccionario.items():
    
    key  = datos[0] # KEY = LLAVE
    value  = datos[1] # VALUE = VALOR
    # KEY es para la variable ; .item () es para el valor que tiene guardada la variable

    print((f"La clave es : {key} ; el valor es: {value}"))

