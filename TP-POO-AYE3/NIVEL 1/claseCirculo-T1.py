# Clase Círculo: Crear una clase `Circulo` que reciba el radio como atributo y tenga
# métodos para calcular el área y el perímetro.

import math


pi_redondeado = round(math.pi, 2)

class Circulo:

    def __init__(self,radio):
        self.radio = radio

    def Area(self):

        area = (pi_redondeado * (self.radio**2))

        print(f"El area es: {area}")

    def Perimetro(self):

        perimetro = (2 * pi_redondeado * self.radio)

        print(f"El perimetro es {perimetro}")


radio = int(input("Digite el radio del circulo: "))

pasoRadio = Circulo(radio)

pasoRadio.Area()
pasoRadio.Perimetro()
