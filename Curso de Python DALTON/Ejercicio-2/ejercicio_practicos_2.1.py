
#faslto el profe y los pibes van a armar la clase

#Vamos a pedir la edad y el nombre de los compañeros que vinieron a aclases 

#Creamos una funcion la cual es catidad de copañeros y 
def obtener_cantidad_de_compañeros(cantidad_de_compañeros):
    
    compañeros = [] #Hacemos que compañeros sea una lista

    for i in range (cantidad_de_compañeros): #Iteramos la cantidad de compañersos
        nombre = input("Ingres el nombre: ") #Pedimos el nombre 
    
        edad = int(input("Ingres la edad: ")) #Pedimos la edad
        
        compañero = (nombre,edad) #Creamos la variable compañeros y le asigamos los valores de nombre y edad
        
        compañeros.append(compañero) #Agregamos la viable compañero a la LISTA compañeros
        
    compañeros.sort(key=lambda x:x[1]) #Ordenamos los compañeros por la edad
    
    asistente  = compañeros[0][0] #El asistente va a hacer el mas pequeño, con el primer 0 tomamos el nombre y el segundo 0 la edad
    
    profesor = compañeros[-1][0] #Y el profesor va a hacer el más grande, con el -1 tomamos el ultimo valor y el 0 el nombre
    
    return asistente,profesor #Retornamos el valor de asistente y el valor de profesor

#Aisgnamos las vairables profesor y asistente que de vuelve la funcion obtener cantidad de compañeros

#El 5 va a hacer la cantidad de iteracion que se van a hacer en la funcion
#Desempaquetamos lo que retorna la funcion
asistente,profesor = obtener_cantidad_de_compañeros (5) 

#Imrpimimos el valor profesor que sacmos de la funcion y el asistente

print(f"El profesor es {profesor} y el asistente es {asistente}")