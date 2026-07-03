# Creá una función lambda que reciba una cadena de texto y devuelva True si la palabra
# empieza con la letra P (mayúscula) y False en caso contrario.


print("Este programa detecta la palabra empieza con P (mayúscula)")

palabra = input("Ingrese una palabra: ")



mayusculaP = lambda p: p.startswith("P")


print(mayusculaP(palabra))

