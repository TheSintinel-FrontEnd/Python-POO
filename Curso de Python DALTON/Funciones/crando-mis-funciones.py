
#Para crear mis propias funciones se una el DEF 

def hola (): #Creamos la funcion
    
    numero = (12,77)
    suma = sum (numero)
    print(suma)
    print("Muy buenas tardes") #Declaramos lo que queremos que haga la funcion
    

hola() #Llamamos a la funcion para que ejecute todo lo que esta adentro de ella


def saludar_sexo (nombre,sexo):
    
    sexo = sexo.lower() #Conviertidno en minusculas el adjetivo 
    
    if (sexo == "mujer"): #Si es MUJER ejecuta esto
        
        adjetivo = "Reina" #Imprime REINA
        
    elif (sexo == "hombre"):#Si es Hombre ejecuta esto
        
        adjetivo = "Tiran" #Imprime TITAN
        
    else: #Si no se identifica con ninguno ejectutato
        
        adjetivo = "persona favorita" #Imrpime CRACK
        
        
    print(f" Hola {nombre}, mi {adjetivo} como andas?")

#Otorgamos "VARIABLES" a la "FUNCION" "SALUDAR_SEXO" para que identifique con que elementos estamos trabajando

saludar_sexo ("Alfredo","hombre") 

saludar_sexo ("Iliana","Mujer")

saludar_sexo("Yamel","")

print("---------------------------------")

def creando_contraseña_random (num): #Creo la funcion 
    
    chart = "abcdefghijklmnopqrstxvwyz" #Creo una cadena de caracteres para ir variando la contraseña
    num_entero = str (num) # Convierto el num en un caracter
    num = int (num_entero[0]) # Convierto num en un entero y lo valorizo en 0
    c1 = num -2 # el numero asignado le resto
    c2 = num #el numero asignado lo dejo
    c3 = num -8 #el numero asignado le resto 9
    
    contraseña = f"{chart[c1]} {chart[c2]} {chart[c3]} {num *2} " # creo la contraseña con los elementos ya creados
    
    #el num por 2 , es el valor que asigno multiplicandolo por 2
    
    return contraseña,num #retorno el contraseña, paara trabajar con ella fuera de la funcion creada

#una vez ya acada la funcuncion , podemos usar la contraseña porque devolvimos

#asigno un valor para crear la contraseña (dpendiendo del numero crea diferentes contraseñas)
#desempaquetando la funcion
password,numero_utilizado = creando_contraseña_random (43) #llamo a la funcion y asigno el numero entre parentesis para utilizarla en la funcion
#unicamente toma el primer valor del numero dado
frase = f"tu contraseña es {password}" #Creo una frase que contrenga la contraseña

print(frase) #Imrpimo la frase que cntiene la contraseña}
print(f"el numeor utilizado es: {numero_utilizado}")

print("----- sabes que es -------")

que_es = type(frase)

print(f"es : {que_es}") #SRT o cadena de caracteres


def suma (nombre,*cifra): #hago la funcion 
    
    return f"{nombre}, la suma de los numero es {sum(cifra)}"  #declaro lo que quiero que haga una suma y me la retorne

resultado = suma("Alfre",4,5,78,2,77,31) #doy las cifras que quiero que me sume

print(resultado) #Imprimo el resultado de la suma de lso numeros dados

