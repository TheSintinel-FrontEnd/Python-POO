#El Filtro de Nombres: Crea una función que reciba una lista de nombres y
#devuelva solo aquellos que comiencen con una vocal y tengan más de 5
#caracteres.

def filtroDeNombres():

    listaNombresFiltro = []

    for num in range(5):
        print("Cargue un lista con 5 nombre")
        nombresParaLalista = input("Ingese un numero: ")
        listaNombresFiltro.append(nombresParaLalista)

    for nombre in listaNombresFiltro:
        #nombres = listaNombresFiltro[1]
        nombreCapi = nombre.capitalize()
        vocales = ["A","E","I","O","U"]
        
        if nombreCapi.startswith(tuple(vocales)) and len(listaNombresFiltro)>=5:
                print(f"Su nombre {nombre} tiene como primera letra una VOCAL y es mayor a 5 caracteres")
        


##si el nombre emepiza con una vocal, comparación de cadena con vocal

filtroDeNombres()