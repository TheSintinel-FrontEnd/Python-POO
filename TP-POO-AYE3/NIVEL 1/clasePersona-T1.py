# Clase Persona: Crear una clase `Persona` con atributos `nombre`, `edad` y un método
# que imprima los datos.


class Personsa:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):

        print (f"El estufiante {self.nombre} tiene {self.edad} años")


nombre = input("Digite el nombre del alumno: ")
edad = int(input ("Digite la edad del alumno: "))


datosPersonsa = Personsa(nombre,edad)

datosPersonsa.mostrarDatos()