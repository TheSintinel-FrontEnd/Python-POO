# Tienda con Productos: Crear una clase `Tienda` que almacene productos, con métodos
# para agregar, eliminar y listar productos.

#re complicado profe



class Productos:

    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrarProducto(self):

        print(f"El producto es {self.nombre} y sale {self.precio}")


class Maxikiosco:
    def __init__(self):
        self.productos = []

    def agregarProductos(self,producto):
        
        self.productos.append(producto)
    

    def eliminarProductos(self,indice):

        if 0 <= indice < len(self.productos):
            eliminando = self.productos.pop(indice)
            print(f"{eliminando.nombre} eliminado.")
        else:
            print("Opcion invalida.")

    def listarProductos(self):
        for i, producto in enumerate(self.productos):
            print(f"{i+1}. {producto.nombre}")

    

#Ingreamos el primer productos

nombre = input("Digite el nombre del productos: ")

precio = int(input("Ingrese el valor del producto: "))

ingProducto = Productos(nombre,precio)

ingProducto.mostrarProducto() #Varificamos su ingreso


#declaramos la instancia de la clase
maxi = Maxikiosco()

maxi.agregarProductos(ingProducto)



#Agregamos 2 productos mas
nombre1 = input("Digite el nombre del productos: ")

precio1 = int(input("Ingrese el valor del producto: "))

ingProducto1 = Productos(nombre1,precio1)

maxi.agregarProductos(ingProducto1)

nombre2 = input("Digite el nombre del productos: ")

precio2 = int(input("Ingrese el valor del producto: "))

ingProducto2 = Productos(nombre2,precio2)

maxi.agregarProductos(ingProducto2)



#Listamos el total de los productos agregador

maxi.listarProductos()

opcion = int(input("¿Qué producto desea eliminar?: "))


#Y a por eleccion del indice eliminamos uno de los 3 prductos

maxi.eliminarProductos(opcion-1)