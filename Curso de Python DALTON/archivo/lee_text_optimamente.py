
#Abrimos y cerramos el txt, y también el cambiamos el nombre con el "as"

with open ("archivo\\Boca.txt",encoding="UTF-8") as Boca:
    #Le asignamos otra variables y lo leemos
    BOCA = Boca.read()
    #Imprimimos el txt
    print(BOCA)

#No es necesario cerrarlo al usar "with open" (porque se cierra solo)
