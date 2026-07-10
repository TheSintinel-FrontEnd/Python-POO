# Herencia con clase Estudiante: Crear una clase `Estudiante` que herede de `Persona` y
# agregue atributos como `curso` y `nota_final`.


class Personsa:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def datos (self):

        print (f"Mi nombre es {self.nombre} y tengo {self.edad}")


class Estudiane(Personsa):

    def __init__(self, nombre, edad,curso,nota_final):
        super().__init__(nombre, edad)
        self.curso = curso
        self.nota_final = nota_final

    def datosEstudiantes(self):

        print (f"Soy del curso {self.curso} y mi nota es {self.nota_final}, como ya dije soy {self.nombre} y tengo {self.edad} años")


nombre = input("Digite un nombre: ")

edad = int(input("Digite una edad: "))

ingPersonsa = Personsa(nombre,edad)

ingPersonsa.datos()

curso = input("Digite el curso: ")

nota_final = int(input("Digite la nora final: "))

ingEstud = Estudiane(nombre,edad,curso,nota_final)

ingEstud.datosEstudiantes()