#Crenado funcion que sumer numeros
def suma_dos ():
    #Iniciando el bucle
    while True:
        #Pidiendole al usuario numero
        a = input ("Numero 1: ")
        b = input ("Numero 2: ")
        #Intentando convertirlos a enteros u sumarlos
        try:
            resultado = int (a)+ int (b)
        #Si lanza una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("Te pedi nu numero")
            print(f"Eror {e}")
            print(f"Error {type(e).__name__}")
        #Si todo salio bien, terminar el bucle
        else:
            break
        finally:
            print("Finally se ejecuta siempre")
        
    return resultado

#Imprimiendo la funcion (resultado)
print(suma_dos())