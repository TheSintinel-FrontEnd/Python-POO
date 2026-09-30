#Creando un bucle FOR IN para iterar

# LISTAS

animales = ["gato","perro","tortuga","peces"] #Arreglo de animales

numeros = [10.28,49,90]  #Arreglo de numeros

#TUPLAS

animales = ("gato","perro","tortuga","peces") #Arreglo de animales

numeros = (10.28,49,90)  #Arreglo de numeros

#Al iterar se con el bucle FOR funiona de la misma manera si son LISTAS O TUPLAS



#ANIMAL se va a ejecuar la cantidad de veces que ANIMALES tenga variables ejmeplo: si ANIMALES TIENE 5 VARIABLES, ANIMAL se va a ejecutar 5 veces
#Y la variable ANIMAL solo se puede utilizar en este bucle, y no fuera de él
print("----------------------------")

for animal in animales:   #Recoro el arreglo de anmales
    
    #Si imprimo ANIMALES, me inprime la lista 4 veces 
    #En cambio si le digo que imprima ANIMAL me imprime los datos (animales), 1 por cada renglon
    print(f"Ahora la variable animal es igual a {animal}" ) #imrpimo
    
print("----------------------------")

for num in numeros: #Recorro el arreglo de numeros
    resultado = num * 2  #Multiplico el arreglo por 2
    print(resultado)  #Imrpimo

print("----------------------------")

for animal,num in zip(animales,numeros):
    
    #Recorro los 2 arreglos (LISTAS).
    
    print(f"Lista 1 {animal}") #Diferenciar los arreglos entre 1 y 2.
    print(f"Lista 2 {num}")
    
print("----------------------------")    


#Si le ponemos 1 parametrso va desde 0 hasta el numero que le dimos como parametro
for numo in range(2,8): #Itero los numeros del 2 al 8 (enteros)
    
    print(numo) #Imprimo del 2 al 8 
    
print("----------------------------")    


#forma no correcta de recorrer una lista con su indice

for num in range(len(numeros)):
    print(numeros [num])


print("----------------------------")    

for num in  enumerate(numeros):     #Con la funcion enumarate indicamos que indice tiene la variable
    #Mostrado indice y numero
    print(num) #Imprimos indice y variable (en este caso numero)
    print("----------------------------")    

    
    indice = num[0] #Indice de la variable
    valor = num[1] #Nuemro (valor de la variable)
    
    print (f"el indice es {indice} y  el valor es {valor}")
    print("----------------------------")    

#Usando el ELSE con el FOR

else:
    print("Bucle terminado :) ")
    
print("----------------------------")    

# TODOO LO YA HECHO FUNCIONA EXCATAMENTE IGUAL PARA TUPLAS COMO PARA LSITAS

