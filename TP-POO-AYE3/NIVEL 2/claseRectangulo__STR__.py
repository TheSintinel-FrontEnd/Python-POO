# Clase Rectángulo: Crear una clase `Rectangulo` con atributos `base` y `altura`, y métodos
# para calcular área y perímetro.


class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura


    def Area (self):

        area = self.base * self.altura

        print(f"El Área del rectangulo es {area}")
    
    def Perimetro (self):

        perimetro = 2 * (self.base + self.altura)

        print(f"El Perimetro del rectangulo es {perimetro}")



base = int(input("Digite la base del rectangulo: "))

altura = int(input("Digite la altura del rectangulo: "))


formulas = Rectangulo(base,altura)

formulas.Area()
formulas.Perimetro()


