
#Encontrando el numero mayor de una lista
#Funciona tanto es una tupla, como en una lista, como en conjunto 

numeros = [10,29,44,8,3,15] #Arreglo de numero

numeroro_mas_alto = max(numeros) #La FUNCION MAX es para encontrar el numero más alto
numeo_mas_bajo = min(numeros) #La FUNCION MIN es para encontrar el numero mas bajo
print(f"El numero más alto que se encontro en el array es {numeroro_mas_alto}")
print(f"El numero más bajo que se encontro en el array es {numeo_mas_bajo}")


#rendondeando a 6 decimales

numero = round(12.89894,6) #El numero que viene despues de la coma es la cantidad de decimales que va a llavar
#En este caso 6 decimales 

print(numero) #Imprimimos el numero ya asignado

#Retorna False --> (cuando le pasamos un ), 0 ,dato vacio , False, ninguno
#Retorna True --> (cuando le pasamos) distinto de 0 , True cadena de carcateres o datos no vacio

resultado = bool(0) #Retorna flase

resultado1 = bool (23) #Retorna True

print(resultado) # Imprimimos False  Bool (booleano)
print(resultado1) # Imprimimos True Bool (booleano)


print("--------------------------")

#Funcion All (compara todos los datos)

resultado_all = all((293,"Hola",{"hey"})) # Todos caracteres verdaderos

resultado_all_1 = all ((0, False ,[])) # Todos caracteres falsos

resultado_all_comprobacion = all ((True, False, 0,12)) # Datos verdaderos y flase

print(f"Imprimimso el resultado de Booleano de {resultado_all}") # Imprime True

print(f"Imprimimos el resultado Booleano de {resultado_all_1}") #Imprime False

print(f"Imprimimos la comprobacion de {resultado_all_comprobacion}") # Imprime false porque los datos asignados son distinto

print("--------------------------")


#Funcion SUM (suma todos los numeros)
#Unicamente tienen que ser numeros , porque si ponemos un dato Booleano, o texto, me devulve una excepcion
numeros_suma = (20,30,1,55) 

resultado_suma = sum(numeros_suma)

print(f"imprimimos la suma del arreglo {resultado_suma}")