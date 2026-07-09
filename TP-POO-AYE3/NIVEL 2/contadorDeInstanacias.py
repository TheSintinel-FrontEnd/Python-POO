# Contador de Instancias: Crear una clase `Contador` que lleve la cuenta de cuántos
# objetos se han creado con ella.


class contadorDeObjetos:

    _total_instancias = 0

    def __init__(self,nombre):
        self.nombre = nombre

        contadorDeObjetos._total_instancias += 1


    @classmethod

    def obtener_total(cls):
        """Metodo de clase para cpnsultar el contador sin crear instancias"""
        return cls._total_instancias
    
    def __str__(self):
        return f"Soy {self.nombre}. Total objetos creador {self._total_instancias}"


print("Esté programa contara cuentas veces se llamo a la instancia de la clase")
nombre = input("Digite un nombre: ")

ingPeronsa = contadorDeObjetos(nombre)

print("Se llamo a la clase ",contadorDeObjetos.obtener_total()," vez")

print(ingPeronsa)

nombre1 = input("Digite otro nombre: ")

ingPersonsa1 = contadorDeObjetos(nombre1)

nombre2 = input("Digite otro nombre: ")

ingPersonsa2 = contadorDeObjetos(nombre2)

print("Se llamo la clase ",contadorDeObjetos.obtener_total(), " veces")