#importando el modulo CSV
import csv
#Leyendo un archivo CSV 

#Abrindo y cerrando el CSV, usando una decoficacion universal "UTF-8" y asignandole el nombre de texto
with open ("archivo\\texto.csv",encoding="UTF-8") as texto:
    #Comprobamos que fue leido
    print("Fue leeido correctamente: ")
    
    # print(texto.read())
    # print(csv.reader(texto))
    
    #Es un iterable asi que lo puedo recorrer con un for
    #Asigando una variable text "de texto", para que lea el CSV
    text = csv.reader(texto)
    #Hacemos un bucle para iterar (for)
    for read in text: #Iteramos "read" en "text" que seria "para (for) leer (read) en(in) texto (text)"
        
        print(read) #Imprimimos el CSV
    
    