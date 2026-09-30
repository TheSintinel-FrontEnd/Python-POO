
#Abriendo el archivo (texto_de_boca) con la "a" (escribimos en el txt) y asignamos el nombre Boca con "as"
with open ("archivo\\Texto_de_boca.txt","a",encoding="UTF-8") as Boca:
    
    #Agregando texto con "a" (no sobrescribiendolo como con "w")
    #Usando un bucle (for) para agregar varias lineas
    Boca.write("\n")
    #for i in range (5):
        
   #     Boca.write(f"Linea {i+1} agregada\n")
        
   
    for i in range (5): Boca.write(f"Lineas de codigo {i+1} agragdin\n")
