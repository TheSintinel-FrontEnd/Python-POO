#creando mi propia excepcion personalizada
class MiExcepcio(Exception):
    def __init__(self,err):
        
        print(f"Impresionante, cometiste el siguente error : {err}")

#Lanzando mi propia excepcion
#raise MiExcepcio("Aprende como dividir")

try:
    raise ZeroDivisionError("Que boludito, dividiste por 0")
except:
    print("Como vas a divir por 0")
