
#Creamos una funcion la cual nos devulva losnuemros primos

#Entre 0 y el numero que le asignemos


def es_primo (num): #Creamos la funcion es primso y le pasamos un valor 
    
    for i in range (2,num-1): #I va a hacer 2 , num-1 , va a hacer el numero que le dimos -1
    
        if  num %i ==0:  #Si el numero que le dimos es divisible por i (2) y el resultado da 0
            return False #retorna falso
    return True #y sino retorna verdadero


def primos_hasta (num): #Creamos otra funcion la cual nos muestra a hasta que numero es primo el muero dado
    
    primos = [] #creamos una lista que se llame primos 
    for i in range(3,num+1): #iteramos el resultado de la funcion es primos y que tiene un rango de 3 hasta el numero dada +1 (asi cuenta el numero que le dimos)
        resultado = es_primo(i) #Resultado de los anteriror es primo
        if resultado == True: primos.append(i) # si resultado es verdadero , no lo guaerda en la lista primos
    return primos #retornamos primos

#El numero 13 el el numero que queremos hasta el que llego
resultado = primos_hasta(13) # la virable resultado va a ser lo que nos retorne la funcion primos hasta 

print(f"Los numeros primos son: {resultado}") #Imprimomos la variable resultado que tiene como valor lo retornado en numeros primos


