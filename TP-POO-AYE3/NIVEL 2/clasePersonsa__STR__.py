# Clase Persona: Crear una clase `Persona` con atributos `nombre`, `edad` y un método
# que imprima los datos.

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