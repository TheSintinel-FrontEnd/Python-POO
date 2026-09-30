
diccionario = {
    
    "Nombre" : "Alfredo",
    "Apellido" : "Patiño",
    "Edad" : 22
}

clave = diccionario.keys() # Nos devuelve las variables para iterar

#Nos devuelve lo que hay dentro de la variabel,y si no lo encuntra devuelve un NONE y en vez de una excepcion

clave2 = diccionario.get("edad")

#Eliminando todo el diccionario

#diccionario.clear()

#elimianndo elementos del diccionario con POP

diccionario.pop("Apellido")

#Obteniendo un elemento dict_item iterable (se recorre el elemento para poder poder acceder a cada uno de los elementos)

diccionario_iterable = diccionario.items()

print(diccionario_iterable)

