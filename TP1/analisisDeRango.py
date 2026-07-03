# Análisis de Rango: Dada una lista de 10 números aleatorios, encuentra el valor
# máximo, el mínimo y calcula la diferencia entre ellos.


def analisisDeRango():

    print("Digite 10 numeros, de estos 10 el programa calculara el numero más alto el minimo y la distancia entre ellos")
    listaDeNumeros = []

    for num in range(9):
        
        num = int(input("Ingrese un numero: "))

        listaDeNumeros.append(num)

    print(listaDeNumeros)

    numeroMaximo = max(listaDeNumeros)
    numeroMinimo = min(listaDeNumeros)
    rangoDenumero = numeroMaximo - numeroMinimo
    print("La distancia entre el valor más alto y el minimo es de: ",rangoDenumero)




analisisDeRango()