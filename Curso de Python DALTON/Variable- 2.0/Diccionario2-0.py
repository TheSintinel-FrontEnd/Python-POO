#Creando diccionario con ditc

#No se pueden crear tuplas vacias a no ser que usemos TUPLE
#No podemos crear listas vacias a no ser que usemos list
#No se pueden crear diccionario varicios (sin variabes), da la forma convencional ({}), pero si con "ditc"


diccionario = dict (nombre="Alfredo",apellido = "Patiño") 
#Las listas no pueden ser claves y usamos frezentset para meter conjuntos

diccionario= {frozenset(["Alfredo","Ingeniero"]):"organizador"}

#Creando diccionario con ditc.fromkeys


diccionario= dict.fromkeys (["nombre","apellido","edad"])



print(diccionario["apellido"])



#nombre = input("Inserte el usuario: ")

#apellido = input("Insetar Apellido: ")

#edad = input("Insete su edad: ")
#revision para alguna vez


print(diccionario)