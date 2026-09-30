
#Creando un programa que muestre la serie fibonacci entre 0 y el numero dado


def fibonacci (num): #Creamos la funcion fibonacci
    
    a,b = 0,1 #Declaramos a como 0 y b como 1
    fibonacci_lista = [0]  #Creamos una lista que tenga 0 numeros
    for i in range(num): # Para i en el rango del (numero dado)
        
        if b > num : # Si b es mayor que el numero dado
            return fibonacci_lista #Que retorne fibonacci lista
        
        else: #Y que me agregue el valor de (b) a fibonacci lista 
            fibonacci_lista.append(b) 
            a,b = b,a+b # aca estamos diceindo que a y b es = b que es la suma de a+b

#Separamos b que es la sume entre "a + b = b", para que itere continuamente los resultados hasta que b sea meyor que el numero que dimos (21)

resultado = fibonacci(21) #Declaramos resultado a la funcion y le pasamos el numero (21)

print(f"La serie de fibonacci con el numero dado es: {resultado}") #Imprimimos la serie de Fibonacci

