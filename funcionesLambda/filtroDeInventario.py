# Supongamos que tenés una lista de productos, donde cada producto es un diccionario
# con su nombre y su stock:


productos = [
    {"nombre": "Resistencia", "stock": 50},
    {"nombre": "Capacitor", "stock": 5},
    {"nombre": "Diodo", "stock": 12},
    {"nombre": "Transistor", "stock": 8}
]


# Usá filter() y una función lambda para obtener una lista de los productos que tienen menos
# de 10 unidades en stock (reponer stock).


productosConStock = list(filter(lambda stock: stock["stock"] >= 10, productos))

print(productosConStock)

