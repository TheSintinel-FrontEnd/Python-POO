
#Creamos la clase PADRE

class Personas:
    def __init__(self,nombre,edad,clubDeFutbol):
        self.nombre = nombre
        self.edad = edad
        self.clubDeFutbol = clubDeFutbol
    #Definimos sus acciones
    def hablar(self):
        print("Qué onda?")
    
    def club(self):
        print(f"Soy de {self.clubDeFutbol}")


class Empleado(Personas): #Clase que hereda entre los parentesis
    def __init__(self, nombre, edad, clubDeFutbol,añosTrabajando,salario): #Que es lo viejo y que es lo nuevo
        super().__init__(nombre, edad, clubDeFutbol) #incluimos las herencias

        #Declaramos los nuevos atributos 
        self.añosTrabajando = añosTrabajando
        self.salario = salario
    
    #Declaramos las acciones al estar en una nueva clase 
    def servir(self):
        print("Que vas a tomar?")

    def sinAportes(self):
        print("Llevo trabajando acá 4 años")


ingreso = Personas("Alfredo", "23", "CABJ")

ingreso.club()

ingresoEmpleo = Empleado("Alfredo","23","CABJ" ,"4 años","50.000")

ingresoEmpleo.hablar()

ingresoEmpleo.sinAportes()

ingresoEmpleo.servir()