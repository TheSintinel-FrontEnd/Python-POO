#Matriz de lista (conjunto de datos)

lista = ["Soy Alfredo","Tecnico Electronico",True,1.75] #corchetes

#La tupla No se puede modificar , mientras que la lista SI

tuplas = ("Soy Alfredo","Tecnico Electronico",True,1.75)  #parentesis


#ESTO SI ES VALIDO
lista[3] =  "joya"


#ESTO NO ES VALIDO
# tuplas[3] =  "joya"

#crando un junto (set) (no se puede acceder a elementos por indice, no almacena datos duplicados)

conjunto  = {"Soy Alfredo","Tecnico Electronico",True,1.75} #llave 


#print(conjunto[3]) -> No puede acceder al elemanto

print(conjunto)


#Creando un diccionario (dict) (la estructura es key : value y separamos con comas )

diccionario = {
    
    "nombre" : "Alfredo",
    "titulo" : "Tecnico Electronico",
    "esta_emocionado" : True,
    "altura" : "1.75",
    "Dato_duplicado" : "Alfredo"
}

print(diccionario["titulo"])



