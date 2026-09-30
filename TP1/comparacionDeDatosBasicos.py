# Compresión de Datos Básica: Escribe una función que reciba una lista de
# caracteres repetidos (ej. "a", "a", "b", "c", "c", "c"]) y devuelva una
# lista de sublistas con el carácter y su frecuencia (ej. [["a", 2], ["b", 1],
# ["c" , 3]]).

from collections import Counter

listaDeCaracteresRepetidos = ["a","a","b","c","z","l","p","p","w","w"]


def filtroDeCaracteresRepetidos(lista):

    print("Esta es la lista: ",lista)
    
    cantidadDeCaracteresSinRepetir = []

    conteoDeCaracteres = Counter(lista)

    cantidadDeCaracteresSinRepetir.append(conteoDeCaracteres)

    print(cantidadDeCaracteresSinRepetir)


filtroDeCaracteresRepetidos(listaDeCaracteresRepetidos)




