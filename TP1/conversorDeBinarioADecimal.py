# Conversor de Binario a Decimal: Solicita al usuario una lista de ceros y unos
# (un número binario) y calcula su equivalente decimal manualmente usando ciclos.


def calculadoraDecimal():
    
    valorDecimal = 0
    numeroBinario = int(input("Ingrese un numero binario para convertirlo a decimal: "))

    digitos = list([])
    

    while numeroBinario>0:
        digitos.append(numeroBinario % 10)
        numeroBinario //= 10

    for indice,valor in enumerate(digitos):
        
        posicionDeI = 2**indice

        numValor = posicionDeI * valor

        valorDecimal = valorDecimal + numValor
        print(valorDecimal)

        
    print(valorDecimal)


calculadoraDecimal()