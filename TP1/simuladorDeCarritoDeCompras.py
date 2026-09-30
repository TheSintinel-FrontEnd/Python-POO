# Simulador de Carrito de Compras: Crea un programa que permita al usuario
# ingresar nombres de productos y sus precios hasta que escriba "fin". Al terminar,
# debe mostrar el total gastado y el producto más caro.


listaDeCompras = list([])


def carritoDeCompras(lista):
    suma = 0
    contenedorAnterior = 0

    nombreProducto = input("Ingrese el nombre de su producto: ")

    while nombreProducto != "fin":

        
    
        precioProducto = int(input("Ingrse el precio del producto: "))
        
        nombreProducto = input("Ingrese el nombre de su producto: ")

        suma = precioProducto + suma



    
    print(f"El valor de todos los productos es ",suma)







carritoDeCompras(listaDeCompras)
