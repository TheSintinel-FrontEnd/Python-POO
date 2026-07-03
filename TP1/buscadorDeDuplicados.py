#Buscador de Duplicados: Dada una lista con elementos repetidos, genera una
#nueva lista que contenga únicamente los elementos que aparecían más de una vez,
#pero sin repetirlos en el resultado final.



listaRepetidos = list([1,1,1,1,4,"hola mundo", "Hola mundo"])


def filtroDeRepeticion (a):
    
    listaSinRepetidos = list(set(a))
            
    print(listaSinRepetidos)    


filtroDeRepeticion(listaRepetidos)
