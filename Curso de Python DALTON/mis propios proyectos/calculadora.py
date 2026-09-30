
#Calculadora en Python


valor1 = input("Digite un valor: ")      #Pedrile al usuario por comando

valor2 = input("Digite un segundo valor: ")   #Pedirle al ususario por comando


#Convertirlo el string en numero flotante (también se podria convertir en entero, pero a la hora de hacer divison es mejor un flotante)

numero1 = float(valor1)

numero2 = float(valor2)

#Suma


suma = numero1 + numero2

print(f"El resultado de la suma entre los digitos datos es  {suma}")


#Resta


resta = numero1 - numero2


print(f"El resultado de la resta entre los digitos datos es  {resta}")


#Multiplicacion

mult = numero1 * numero2


print(f"El resultado de la multiplicacion entre los digitos datos es  {mult}")


#Division

Divi = numero1 / numero2

aprox = Divi * 10 / 10  # Aproximamos el valor a su maxima expresion 


print(f"El resultado de la division entre los digitos datos es  {aprox}")



