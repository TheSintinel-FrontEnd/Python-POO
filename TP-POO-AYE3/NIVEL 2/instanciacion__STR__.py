# Instanciación: Crear al menos tres objetos de la clase `Persona` e imprimir sus datos con
# el método correspondiente.


# Método `__str__`: Modificar las clases anteriores para que incluyan un método `__str__`
# que retorne una representación legible del objeto.

class Personsa:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):

        return (f"El estudiante {self.nombre} tiene {self.edad} años")


nombre = input("Digite el nombre del alumno: ")
edad = int(input ("Digite la edad del alumno: "))


datosPersonsa = Personsa(nombre,edad)

print(datosPersonsa)

nombre1 = input("Digite el nombre del alumno: ")
edad1 = int(input ("Digite la edad del alumno: "))

datosPersonsa1 = Personsa(nombre1,edad1)

print(datosPersonsa1)

nombre2 = input("Digite el nombre del alumno: ")
edad2 = int(input ("Digite la edad del alumno: "))

datosPersonsa2 = Personsa(nombre2, edad2)

print(datosPersonsa2)