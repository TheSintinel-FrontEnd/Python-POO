#aca se calculan las multiplicaciones y las divisiones


def Multi (num1,num2): #Definimos las funcion de Multiplicacion y los valores que le vamos a pasar
    
    multi = num1 * num2  #Hacemos la multiplicacion en los 2 numeros
    
    return f"La multiplicacion de los numeros por si mismos es {multi}" #Retornamos la multiplicacion


def Divi (num1,num2): ##Definimos las funcion Division y los valores que le vamos a pasar
    
    divi = round(num1 / num2,2) #Devidimos los numeros y con el round nos da un valor aprox
    
    return f"La divison de los propios numero es {divi}" #Retornamos la division