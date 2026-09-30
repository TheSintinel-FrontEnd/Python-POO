
class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    
    def hablar(self):
        print("Hola desde B")

class C(A):
    
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    
    def hablar(self):
        print("Hola desde D")


d = D()

d.hablar()

#Para ver el orden de resolucion de objetos usamos mro

print(D.mro())


#Si quiero llamar a "hola desde B"

#Usamos la clase B, llamamos a su accion y le pasame como referencia de "self" --> "D" que es un objeto ya creadp (que lo tome como referencia, desde punto de partida)
B.hablar(d)

#Podemos llamar a más "Holas"

C.hablar(d)