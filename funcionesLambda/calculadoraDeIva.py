#POR ENÉSIMA VEZ EL PROFE PIDE UNA CALCULADORA DE IVA PERO QUIEN SOS EL CONTADOR DE MILEI ?????


# Escribí una función lambda que reciba el precio de un producto y devuelva el precio final
# con el IVA (21%) incluido.



print ("Esté programa devuleve el precio del producto que usted digite con el IVA incluido")



precioProducto = int(input("Escriba el precio del producto: "))


precioConIva = lambda p: p + (p * 0.21)


print("Esté es su producto con el IVA incluido: ",precioConIva(precioProducto))