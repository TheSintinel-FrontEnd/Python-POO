
#Calculadora de Promedio Móvil: Escribe un programa que reciba una lista de
#números y devuelva una nueva lista donde cada elemento sea el promedio entre el
#número actual y el anterior (el primero se queda igual).


cantNum = (10,20,1,3,9,77,30,11)

def promedioDeNumeros (a):
        i=1
        promLista = 0
        antNum = 0
        listaDePromedios = list([])
        for num in enumerate(a):
            
            antNum= promLista
            promLista = (num[1]+antNum )/ i
            antNum = promLista
            i += 1
            
            listaDePromedios.append(promLista)
            print(listaDePromedios)
            


promedioDeNumeros(cantNum)

