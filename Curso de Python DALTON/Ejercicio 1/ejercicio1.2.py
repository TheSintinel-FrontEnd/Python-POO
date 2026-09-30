# 1) 

frase = input ("Decime una frase y te calculo cuando tardarias si tuvieras que decirla: ")

palabras_separadas =  frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")

print(f"Dalto lo dira en {cantidad_de_palabras/2*1.3} segundo en decirlo")


if cantidad_de_palabras > 120:
    print("Para flaco no te pedi un testamento :/")
    
elif cantidad_de_palabras < 100:
    print("No son muchas palabras")
    
else:
    print("casi nada escribiste")    
    
