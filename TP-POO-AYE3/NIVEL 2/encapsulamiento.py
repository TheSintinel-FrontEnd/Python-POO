# Encapsulamiento: Implementar atributos privados para `nombre` y `edad` en la clase
# `Persona` y proporcionar métodos `get` y `set`.



class Persona:

    def __init__ (self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad (self, valor):
        """condicionamos el valor que puede tener edad"""
        if valor < 0:
            raise ValueError("Error la edad no puede ser negativa")
        if valor >120:
            raise ValueError ("La edad parace invalida")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        if not isinstance (valor, str) or len(valor)==0:
            raise ValueError ("El nombre no puede ser una cadena vacia")
        self._nombre = valor


nombre = input ("Digite el nombre de a personas: ")
edad = int(input ("Digite la edad: "))


ingPersonsa = Persona(nombre,edad)

print(ingPersonsa.nombre)
print(ingPersonsa.edad)