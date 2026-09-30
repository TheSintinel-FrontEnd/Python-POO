
#Funcion LABDA
# Se usa para algo sencillo (rapido) y retornan aumaticamente el valor
print("---------FUNCION LABDA----------")
multiplicacion_labda  = lambda x : x*2
sumalbda = lambda x : x+3
restalabda = lambda x : x-2
divisionlabda = lambda x : x/2
#Primero el nombre de la funcion y despues entre " () " por lo que queres multiplicar
print(f"La multiplicacion es: {multiplicacion_labda(5)}") #Imprimimos las Multiplicacion
print(f"La sumatoria es :{sumalbda(5)}") #Imprimimos la suma
print(f"La resta es : {restalabda(5)}") # Imprimimos las resta
print(f"La division es: {divisionlabda(5)}") #imprimimos la division

print("--------FUNCION-FILTER----------")

#Creando una lista de numero


numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


#Filtrando los numeros pares

def es_par (num): #Creamos una funcion
    
    if (num%2 ==0): #Si el resto de la division por 2 da 0
        return True #Retorna TREU

# Asignando los numeros pares (retornados como TRUE)
# Y filtrandolos con el funcion y la lista de numeros anteriormente creada

def es_impar (num):
    if (num%2 == 1):
        return True

numeros_par = filter(es_par,numeros) 

numeros_impar = filter (es_impar,numeros)
print("Numeros Pares: ")
print(list(numeros_par)) #Imrpimimos en forma de lista los numeros pares almacenados en la variable numeros_par
print("Numeros Impares: ")
print(list(numeros_impar)) #Imprimimos en forma de lista los numeros impares almacenados en la variable numeros_impar


#Combinando las FUNCIONES LABDA y FILTER

print("----CONVINACION DE FUNCIONES-----")
numeros2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


numero_pares = filter (lambda numeros2: numeros2%2 == 0,numeros2)

print("Numeros Pares: ")

print(f"Los numeros pares son : {list(numero_pares)}")

numero_impares = filter (lambda numeros2: numeros2%2 == 1,numeros2)



print(f"Los numeros impares son :{list(numero_impares)}")