
#Creando una funciond e 3 argumentos


def frase (nombre,apellido,adjetivo = "tonto"):
    #Apesar de tener el tonto asignado arriba , al momento de pasarle los parametros, me lo sobre escribe con agradable
    return f"Hola {nombre} {apellido} sos muy {adjetivo}"

#Keybord argument (argumento del teclado)
frase_total = frase (nombre = "Alfredo",apellido = "Patiño",adjetivo = "agradable") # Paso las variables

print(frase_total)
