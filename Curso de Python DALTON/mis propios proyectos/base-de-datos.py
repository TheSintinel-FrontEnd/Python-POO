
#Base de datos

#Creamos una lista donde almacenar los datos

nombre = input("Digite su nombre: ") #Asignamos un nombre
contra = input("Digite una contraseña: ") #Asignamos una contraseña

lista = list([nombre,contra]) #Guardamos los valores ingresdos en la lista

print(f"{lista}") #Verificamos que los datos ingresados esten recorriendo la lista e imprimiendolos

# le preguntamos si quiere moficicar el nombre

valor= input("De sea moficar el nombre , SI o NO: ")
Si = "Si"

if valor == Si:
    nombre = input("Digite el nuevo nombre del usuario: ")
    
# le preguntamos si quiere moficicar la contraseña

valor2 = input("Desea modificar la contraseña: ")

if valor2 == Si:
    contrasela = input("Digite la nueva contraseña: ")

lista = list([nombre,contra])

print(lista)



