
#Creamos la clase 
class Estudiante:
    #creamos su constructor
    def __init__(self,nombre,edad,grado):

        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    #creamos la acción de estudiar
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")



nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = input("Ingrese el grado del estudiante: ")


queHaceElEstudiante = Estudiante(nombre,edad,grado)


queHaceElEstudiante.estudiar()



