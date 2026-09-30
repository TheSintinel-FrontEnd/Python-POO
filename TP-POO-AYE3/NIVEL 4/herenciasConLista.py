# Clase Curso con lista de Estudiantes: Crear una clase `Curso` que contenga una lista de
# objetos `Estudiante`. Agregar métodos para añadir estudiantes y mostrar todos los
# datos.


class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Mi nombre es {self.nombre} edad {self.edad} años")


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []   # Lista de objetos Estudiante

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Curso: {self.nombre}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            estudiante.mostrar()


# Crear estudiantes
e1 = Estudiante("Ana", 20)
e2 = Estudiante("Alfredo", 22)
e3 = Estudiante("Martina", 19)

# Crear curso
curso = Curso("BASE DE DATOOOSSSS")

# Agregar estudiantes al curso
curso.agregar_estudiante(e1)
curso.agregar_estudiante(e2)
curso.agregar_estudiante(e3)

# Mostrar estudiantes
curso.mostrar_estudiantes()