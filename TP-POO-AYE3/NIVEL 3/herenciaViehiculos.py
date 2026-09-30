# Jerarquía de Vehículos: Crear una clase base `Vehiculo` y derivar las clases `Auto` y
# `Moto`. Cada una debe tener métodos distintos.


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def elVehiculo(self):
        return f"El {self.marca} es un {self.modelo}."

# Primera clase hija: Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llama al constructor del padre
        self.puertas = puertas
    
    def abrirPuertas(self):
        print (f"Se abrieron las {self.puertas} del auto")

# Segunda clase hija: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo,cilindrada):
        super().__init__(marca, modelo)  # Llama al constructor del padre
        self.cilindrada = cilindrada
    
    def mostrar_cilindros(self):
        print (f"Cilindrado {self.cilindrada} cc")




auto = Auto("Ford", "Focus", 4)
moto = Moto("Yamaha", "MT-03", 321)


auto.elVehiculo()
auto.abrirPuertas()


moto.elVehiculo()
moto.mostrar_cilindros()