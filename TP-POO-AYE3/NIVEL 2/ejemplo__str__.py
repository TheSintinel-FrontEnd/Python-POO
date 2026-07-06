class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        # Devuelve: "NombreDeLaClase: Nombre (Salario)"
        return f"{self.__class__.__name__}: {self.nombre} (${self.salario})"

class Gerente(Empleado):
    pass  # Hereda __str__ automáticamente

emp = Empleado("Ana", 50000)
ger = Gerente("Carlos", 80000)

print(emp)  # Salida: Empleado: Ana ($50000)
print(ger)  # Salida: Gerente: Carlos ($80000)   