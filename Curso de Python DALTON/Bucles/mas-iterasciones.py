
frutas = ["manzana","banana","uva","pera","mandarina"]

for fruta in frutas : #Iteramos el arreglo
    
    if fruta == "uva": # condcionamos a fruta para que cuando valga UVA la salte e ietere la siguente fruta
        continue #Sentencia CONINUE (evita elementos del arreglo)
    print(f"me voy a comer {fruta}")

for fruta in frutas:
    print(f"Me voy a comer {fruta}")
    if fruta == "pera":
        break #Con un brake termina directamente el codigo
else: 
    print("Se termino") # Este else nunca se va a ejecutar porque esta el BRAKE antes 

print("Bucle termiando ")


#iterando una cadena de texto

cadena = "Hola Alfredo"

for letra in cadena :
    print(letra)



numeros = [2,4,6,10]

numeros_duplicados = [x*2 for x in numeros]
#Primero la expresion matematica y despues el " "ecuacion aritmetica" for (a lo que se envierte(este valor solo es valido en el for)) in (variable)"
# for = para ; in = en . x*2 para(for) x es/en(in) numeros
#X = numeros y se multiplican por (*) 2
print(numeros_duplicados)




