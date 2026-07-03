#Lo mismo que herencia pero ahora desonBOCA en más clases o subclases


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


class Profesion:
    def __init__(self,profe):
        self.profe = profe
    
    def cualEsTuprofesion(self):
        print(f"Mi profesion es {self.profe}")


class NuevoEmpleo(Personas,Profesion):
    def __init__(self, nombre, edad, clubDeFutbol,profe,postulacion):
        Personas.__init__(self,nombre, edad, clubDeFutbol)
        Profesion.__init__(self,profe)

        self.postulacion = postulacion



    #Exite dos formas de llamar a una función que ya ha sido creada
    def club(self):
        print(f"SOY HINCHA DE {self.clubDeFutbol}") #Acá puedo sobreescribirla

    def clubFutbol(self):
        print(f"Soy de {super().clubDeFutbol}")

    #Las dor formas son correctas pero, en el primer caso al usar self puedo crear una nueva función  (sobreescribirla)
    #En cambio si uso super() ya estoy utilizando o llamando a la clase donde se encunetra ese atributo



    def presentarse(self):
        print (f"Hola mi nombre es {self.nombre}, tengo {self.edad}, me quiero postular como {self.postulacion}, porque soy {self.profe}, ")

ingreso = Personas("Alfredo", "23", "CABJ")

ingreso.hablar()

ingresoEmpleo = Empleado("Alfredo","23","CABJ","4 años","50.000")

ingresoEmpleo.sinAportes()

ingresoDeProfesion = Profesion("Analista de Sistemas")

ingresoDeProfesion.cualEsTuprofesion()




ingresoNuevoEmpleo = NuevoEmpleo("Alfredo","23","CABJ","Analista De Sistemas","Profe de Electricidad")

ingresoNuevoEmpleo.presentarse()


#Tips

#verificamos herencia a partir de TRUE o FALSE
herencia = issubclass (NuevoEmpleo,Personas)

#Verificamos INSTACIAS de la CLASE (SI ES UN OBJETO DE CLASE)

#ingresoDeProfesion es un OBJETO de la clase PROFESIÓN?,también comprueba con TRUE y FALSE
instacia = isinstance(ingresoDeProfesion,Profesion)