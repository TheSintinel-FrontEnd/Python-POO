#Asignas valores a vairables de una forma peculiar

#Creando una tupla

datos_en_tupla =  ("Alfredo","Ingeniero Electronico",20)
datos_en_lista = ["Alfredo","Ingeniero",20]
#Los daots son totalmente porporsionales a las variables x datos = x variables
#Desempaquetado
nombre,tuitulo,edad = datos_en_lista

#Mostrando desempaquetado
tupla_numeros = (20,40,90,1)
print(nombre)
print(tuitulo)
print(edad)


#Desempaquetado con bucle for


for num in enumerate(datos_en_tupla):
    
    i = num [0]
    numero = num [1]
    print(f"indice {i} , variable {numero}")

#Usando el ELSE con el FOR

else:
    print("Bucle terminado :) ")
