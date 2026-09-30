# El Traductor de P: Crea un programa que transforme una palabra añadiendo
# una p y repitiendo la vocal después de cada vocal encontrada (Ejemplo: hola -
# hopolapa).



def añadirP():

    vocales = ['a', 'e', 'i', 'o', 'u']
    palabra = input("Ingrese un palabra por cada VOCAL se le añadira una P y se repetira la VOCAL: ")
    palabraMenor = palabra.lower()
    frase = []

    frase.append(palabraMenor)
    
    print(f"Frase original ",frase)

    fraseConP = []

    for letra in palabraMenor: #recorro el arry y le paso los datos a letra
            
            fraseConP.append(letra)

            if letra in vocales: #Si letra se encuentra en la lista de vocales (entra)
                    
                    print("Vocal encontrada", letra) #imprimo la vocal

                    #arregloDeP = "p".join(letra) #join es un separador de cadenas
                    
                    

                    fraseConP.append("p" + letra)
                    
                    

                    
            letrasSinSeparar = "".join(fraseConP) #Borramos los espacios ","
    

    print(f"Frase con P añadida: ",letrasSinSeparar) #Devuleve la cadena con P

añadirP()