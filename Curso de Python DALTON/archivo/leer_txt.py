#usando "open" para abrir un archivo con una codificacion universal (UTF-8)
Boca_sin_leer = open ("archivo\\Boca.txt",encoding="UTF-8")

#Leer el txt completamente
Boca = Boca_sin_leer.read()

#Leer el txt por linea
#lineas = Boca_sin_leer.readlines()

#Leer una sola linea
linea = Boca_sin_leer.readline()

#cerra el archivo (txt) 

Boca.close()

print(linea)
