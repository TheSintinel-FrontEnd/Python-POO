# Método `__str__`: Modificar las clases anteriores para que incluyan un método `__str__`
# que retorne una representación legible del objeto.

import math


pi_redondeado = round(math.pi, 2)

class Circulo:

    def __init__(self,radio):
        self.radio = radio
        self.area = 0
        self.perimetro = 0

    def Area(self):

        self.area = (pi_redondeado * (self.radio**2))

        #print(f"El area es: {area}")
        return self.area

    def Perimetro(self):

        self.perimetro = (2 * pi_redondeado * self.radio)

        #print(f"El perimetro es {perimetro}")
        return self.perimetro

    def __str__(self):
        
        self.Area()
        self.Perimetro()

        return f"El area es {self.area} y el perimetro es {self.perimetro}"

print("Se calculara el AREA y el PERIMETRO")

radio = int(input("Digite el valor del radio del circulo: "))

ingRadio = Circulo(radio)

print(ingRadio)

