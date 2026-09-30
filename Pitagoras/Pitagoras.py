
#Pitagoras

#Importamos sys
import sys
#Importamos las runas de cada funcion (carpeta)
sys.path.append ("C:\\Users\\af449\\Desktop\\Hipotenusa")
sys.path.append ("C:\\Users\\af449\\Desktop\\Cateto1")
sys.path.append ("C:\\Users\\af449\\Desktop\\Cateto2")

import paquete_Cateto1.Cateto1 as cate1
import paquete_Cateto2.Cateto2 as cate2
import paquete_Hipotenusa.Hipotenusa as hipo

#Importamos la funcion y le asignamos otro nombre

#import Hipotenusa as hipo
#import Cateto1 as cate1
#import Cateto2 as cate2


#creamos las variables
num1 = 0
num2 = 0
num3 = 0
Si="Si"
No="No"

#Preguntamos al usuario sobre los datos

condicional_1 = input("Se conoce el cateto 1, Si o No: ")

if condicional_1 == Si:
    num1 = input("Digite el cateto 1: ")
else:
    print("No se conoce el valor del cateto 1")
    
condicional_2 = input("Se conoce el cateto 2, Si o No: ")

if condicional_2 == Si:
    num2 = input("Digite el valor del cateto 2: ")
else:
    print("No se conoce el valor del cateto 2")
    

condicional_3 = input("Se conoce la hipotenusa, Si o No: ")

if condicional_3 == Si:
    num3 = input("Digite el valor de la hipotenusa: ")
else:
    print("No se sabe le valor de la hipotenusa")
    
#Los datos obtenidos los pasamos de "srt" a float
cat1 = float(num1)   
cat2 = float(num2)    
hipotenusa = float(num3)

#Condicionamos las funciones en base a los datos dados por el usuario
#con el "and" estamos diciendo que los 2 condionales se tienen que cumplir para iterar el "bucle-if"
if (condicional_1 == Si and condicional_2 == Si): #el condicional 1 y 2 son Si , ejecuta la funcion
    
    hipote = hipo.Hipotenusa(cat1,cat2) #Asignamos otro nombre a la funcion importada y le pasamos las vairables
    print(hipote) #Imprimimos lo que retorna la funcion
    
    
if (condicional_2 == Si and condicional_3): #el condicional 2 y 3 son Si , ejecuta la funcion
    
    cateo1 = cate1.Cateto1(hipotenusa,cat2) #Asignamos otro nombre a la funcion importada y le pasamos las variables
    print(cateo1) #Imprimimos lo que retorna la funcion


if (condicional_1 == Si and condicional_3 ==Si): #el condicional 1 y 3 son Si , ejecuta la funcion
    
    cateo2 = cate2.Cateto2(cat1,hipotenusa) #Asignamos otro nombre a la funcion importada y le pasamos las variables
    print(cateo2) #Imprimimos lo que retorna la funcion
