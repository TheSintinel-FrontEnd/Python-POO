#Inversión de Frases: Pide al usuario una frase y devuelve las palabras en orden
#inverso utilizando listas (Ejemplo: "Hola mundo" ---> "mundo Hola";).

frases = list([])

frase = input("Ingrese una frase para invertirla: ")

frasesAgregar = frases.append(frase)

fraseInversa = "".join(reversed(frase))

print(fraseInversa)


