# Instanciación: Crear al menos tres objetos de la clase `Persona` e imprimir sus datos con
# el método correspondiente.


class Personsa:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):

        print (f"El estudiante {self.nombre} tiene {self.edad} años")


nombre = input("Digite el nombre del alumno: ")
edad = int(input ("Digite la edad del alumno: "))


datosPersonsa = Personsa(nombre,edad)

datosPersonsa.mostrarDatos()

nombre1 = input("Digite el nombre del alumno: ")
edad1 = int(input ("Digite la edad del alumno: "))

datosPersonsa1 = Personsa(nombre1,edad1)

datosPersonsa1.mostrarDatos()

nombre2 = input("Digite el nombre del alumno: ")
edad2 = int(input ("Digite la edad del alumno: "))

datosPersonsa2 = Personsa(nombre2, edad2)


datosPersonsa2.mostrarDatos()