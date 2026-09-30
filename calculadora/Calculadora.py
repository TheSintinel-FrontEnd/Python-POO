
#Importamos el sys (sistema)
import sys

#Importamos las rutas (carpetas) de cada funcion
#sys.path.append ("C:\\Users\\af449\\Desktop\\Calculadora")
sys.path.append ("C:\\Users\\af449\\Desktop\\SumayResta")
sys.path.append ("C:\\Users\\af449\\Desktop\\DiviyMulti")
sys.path.append ("C:\\Users\\af449\\Desktop\\DbajayExpo")

#Importamos la funcion que tenga cada carpeta y con el "as" le asignamos un valor más corto
import suma_resta as cap1 
import multi_divi as cap2
import DBaja_Expo as cap3

#Le pedimos al usuario que nos de los valores
a = input ("Digite el primer numero: ") 
print("\n")
b = input("Digite el segundo numero: ")
print("\n")

#Los volvemos valores flotantes (el import los hace srt, por eso los cambiamos)
num1 = float(a) 
num2 = float(b)

print("-------------")

#Pasamos los numeros a las funciones (ya convertidos en flotantes)
Sumatoria = cap1.Suma(num1,num2) 
Restaa = cap1.Resta (num1,num2)
Multiplicacion = cap2.Multi(num1,num2)
Divison = cap2.Divi(num1,num2)
Exponente = cap3.Expo(num1,num2)
Divibaja = cap3.Dbaja(num1,num2)

#Mostramos en pantalla las funciones

print(Sumatoria)
print("-------------")

print(Restaa)
print("-------------")

print(Multiplicacion)
print("-------------")

print(Divison)

print("------Para la division baja se uso el 2-------")
print(Divibaja)

print("-------Para el exponente se uso el 2----------")
print(Exponente)
print("-------------")
