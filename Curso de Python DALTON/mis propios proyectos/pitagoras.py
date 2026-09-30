
#Pitagoras

#creamos las variables

cateto1 = 0
cateto2 = 0
hipotenusa = 0
Si="Si"
No="No"

#Preguntamos al usuario sobre los datos

condicional_1 = input("Se conoce el cateto 1, Si o NO")

if condicional_1 == Si:
    cateto1 = input("Digite el cateto 1: ")
else:
    print("No se conoce el valor del cateto 1")
    
condicional_2 = input("Se conoce el cateto 2, Si o No: ")

if condicional_2 == Si:
    cateto2 = input("Digite el valor del cateto 2: ")
else:
    print("No se conoce el valor del cateto 2")
    

condicional_3 = input("Se conoce la hipotenusa, Si o NO")

if condicional_3 == Si:
    hipotenusa = input("Digite el valor de la hipotenusa: ")
else:
    print("No se sabe le valor de la hipotenusa")
    
    
numero1 = float(cateto1)   
numero2 = float(cateto2)    
numero3 = float(hipotenusa)
    
valor1= numero1**2 + numero2**2 #Esto es la hipotenusa

valor2 = numero3 / numero1**2 #Esto es cateto 2

valor3 = numero3 / numero2**2 #Esto es cateto 1


if valor1 >=1:
    print(f"El valor de la hipotenusa es {valor1}")

if valor2 >= 1:
    print(f"El valor de la hipotenusa es {valor2}")

if valor3 >= 1:
    print(f"El valor de la hipotenusa es {valor3}")



