
#Abriendo el archivo (texto_de_boca) con la "w" (escribimos en el txt) y asignamos el nombre Boca con "as"
with open ("archivo\\Texto_de_boca.txt","w",encoding="UTF-8") as Boca:
    
    #Es importante saber que si "write" o "w" no encuentra el .txt lo crea y si lo encuntra lo sobre escribe
    #También se acumula su propio metodo, es decir, al a ver 2 o más write , no se sobre escribe a si mismo;
        # si no que se juntan los textos acumulados al finalizar el codigo 
    #Sobre escribiendo el archivo    
    #  Boca.write("Dale Boca Dale Boo")
    
    #Agregando 2 lineas con writelines
    
    Boca.writelines(["Boca mi buen amigo esta campaña volveremos a estar contigo\n","Se viene Bocaaaaa"])
    
    #Agregando otras 2 lineas
    Boca.writelines ([" Y vamos todos pongamos una luca , para que el Duka se compre una peluca\n", "A los de boca no nos diciplina NADIE"])
    