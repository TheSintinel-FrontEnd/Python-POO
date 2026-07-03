
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def nombreEdad(self):
        print(f"Mi nombre es {self.nombre} y mi edad es {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def miGrado(self):
        print(f"Mi grado es {self.grado} y mi nombre es {self.nombre}")



p = Persona("Alfredo", 23)

p.nombreEdad()
print("\n")
e = Estudiante("Alfredo",23,"3ro")
e.miGrado()
