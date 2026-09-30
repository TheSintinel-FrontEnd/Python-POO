#Crenado un conunto con set
    
#No puede a ver una lista deontro un conjunto , porque la lsita es mutable en cambio el conjuntos no lo es    
conjunto = set({ "Dato1","dato2"})


#Metiendo un conjunto dentro de otro conjunto


conjunto1 = frozenset(["dato1","dato2"]) #FROZENTEN SET == Conjunto congelado
conjunto2 = {conjunto1, "dato3"} #No se pueden meter conjuntos dentro de otros conjuntos

print(type(conjunto))
print(conjunto)

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando que un conjunto es un subconjunto
#Conjunto 2 es un SUBCONJUNTO DE 1
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1


#Verificando si es un super conjunto
#Conjunto 2 es un SUBCONJUNTO DE 1
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 < conjunto1


#verificar si hay algun numero en comun
#Esto es para ver si datos almacenas dos identicos basta con que alla 1 dato igual para que me devuela FALSE
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)
