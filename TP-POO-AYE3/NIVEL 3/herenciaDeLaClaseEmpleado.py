# Clase Empleado: Crear una clase `Empleado` que herede de `Persona`, agregue `sueldo` y
# un método para calcular bonificaciones.


class Personsa:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def datospersona(self):
        print(f"mi nombre es {self.nombre}")
    

class Empleado(Personsa):
    def __init__(self, nombre,sueldo, anos_empresa):
        super().__init__(nombre)
        self.sueldo = sueldo
        self.anos_empresa = anos_empresa
    
    def bonificacion(self):
        
        if (self.anos_empresa <= 5):

            nuevoSueldo = self.sueldo * self.anos_empresa

            print(f"Usted {self.nombre}, su sueldo es {self.sueldo} y ahora es {nuevoSueldo}")

        elif(self.anos_empresa >= 10):
        
            nuevoSueldo = self.sueldo * self.anos_empresa

            print(f"Usted {self.nombre}, su sueldo es {self.sueldo} y ahora es {nuevoSueldo}")

        


nombre = input("Digite el nombre del empledo: ")

ingPersonsa = Personsa(nombre)

ingPersonsa.datospersona()



sueldo = int(input("Digite el sueldo del empleado: "))

anosempresa = int(input("Cuantos años en la empresa ah estado trabajando?: "))

ingEmpleado = Empleado(nombre, sueldo, anosempresa)

ingEmpleado.bonificacion()