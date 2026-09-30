

class Animal:
    def __init__(self,comer, **kwargs):
        self.comer = comer
        super().__init__(**kwargs)

    def come(self):
        print(f"El animal come {self.comer}")


class Mamifero(Animal):
    def __init__(self,amamantar, **kwargs):
        super().__init__(**kwargs)
        self.amamantar = amamantar


    def Amamantar(self):
        print(f"Esta amamntando {self.amamantar}")

class Ave(Animal):
    def __init__(self,volar,**kwargs):
        super().__init__(**kwargs)
        self.volar = volar

    def Volar(self):
        print(f"Esta volando {self.volar}")


class Murcielago (Mamifero,Ave):
    def __init__(self, comer, amamantar,volar):
        super().__init__(comer=comer,amamantar=amamantar,volar=volar)
        
    def acciones(self):
        print(f"El Muercielago come {self.comer}, amamanta {self.amamantar} y vuela a {self.volar}")



m = Murcielago("carne", "leche", "30km")

m.acciones()

print("\n")

print(Murcielago.mro())