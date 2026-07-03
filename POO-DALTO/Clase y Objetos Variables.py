
class celularesFabrica():
    #__init__ es un metodo COSTRUCTOR con el CREAMOS VARIABLES PARA OBJETOS
    def __init__(self,marca,modelo,camara):
        #Aca creamos sus propiedades en forma de variable para referenciar a los datos
        #en este caso nosotros referenciamos a los metodos (atributos en realidad) que va a tener un celular para que cuando le pasemos la vairables (atributo) se autoreferencien

        self.marca = marca
        self.modelo = modelo
        self.camara = camara

        #Para las acciones que puede realizar un celular (utilizamos metodos que no son más que funciones)
        #Para que se pueda ejecutar la acción (función) necesimos indicarle al objeto que se tiene que autoreferenciar con SELF

    def llamar(self):
        print(f"Piiii piiii llamando al 2932010101 desde su {self.modelo}")
    
    def cortarLlamada(self):
        print(f"Usted a cortado la llamada desde tu {self.modelo}")




celularSamsung = celularesFabrica("Samsung", "S23 Ultra", "50MP")
celularAppel = celularesFabrica("Appel", "Iphone 13 Pro Max", "45MP")

print(celularAppel.modelo)

celularAppel.llamar()

celularAppel.cortarLlamada()






