
#LIST es una funcion para crear una lista

lista = list(["Hola","Alfredo",20])   
lista2 = list([23.2354,2023,23])

#Devuelve la cantidad de elementos de la lista

cantidad_de_elementos = len(lista)    

#Agregando un elemntos a la lista

agregando_con_append = lista.append("jajajaja")

#Agregando un elemento a la lista en un indice espasifico

lista.insert(2,"Buen dia")

#Con extend agregamos varios elementos (agregamos una lista)


lista.extend(["Holaaaa",2023,True])
lista2.extend([True,False,False])

#Eliminando un elemntos de la lista (por su indice)

#  print(len(lista))  nos dice cuantos elementos tenia antes de eliminarlo

lista.pop(6)   # -1 para eliminar el ultimo elemento de la lista, -2  para el anteultimo y asi sucesivamente


#revomiendo un elemnto de la lista por su valor , si no existe nos lanza una excepcion

lista.remove("Buen dia")


#Eliminando todos los elemntos de la lista

# lista.clear()


#ordenando la lista  (si usamos el parametro reverseTrue lo ordena en reversa)
#La lista no puede contener string
lista2.sort()

# lista2.sort(reverse=True) ondena de manera invertida la lista de forma asendente

#Inviertiando los elementos de una lista

lista.reverse() #No importa que esten en orden la lista, lo que hace es revertir la lista

print(lista)



