
#Aca se calcula la division baja y el exponente


def Dbaja (num1,num2): #Definimos las funcion de Division Baja y los valores que le vamos a pasar
    
    dbaja1 = (num1 // 2) #Hacemos la division baja con el num1 y el 2
    dbaja2 = (num2 // 2) #Aca los mismo pero con el num2
    
    return f"la divison baja del primero numero es {dbaja1} y del segundo {dbaja2}" #Retornamos ambos valores

def Expo (num1,num2): #Definimos las funcion de Exponentey los valores que le vamos a pasar
    
    expo1 = num1 ** 2 #Hacemos con el num1 su exponente a la 2
    expo2 = num2 ** 2 #Hacemos con el num2 su exponente a la 2
    
    return f"el exponente del primero es {expo1} y del segundo es {expo2}" #Retornamos ambos valores
