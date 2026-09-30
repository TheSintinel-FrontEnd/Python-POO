# VARIABLE = DATO . METODDO ()   Estructura DE METODO / PARAMETROS
# VARIABLE = FUNCION.( DATO )    Estructra de FUNCION

cadena1 = "Hola,Soy,Alfredo"
cadena2 = "bienvenido maquina"
numero = "65"
numerico = "HolaMundo"

resultado = dir(cadena1) # Devuelve los diferentes atrivuos que puede hacer el objeto (es una funcion)

Mayus = cadena1.upper() # Convierte todo en mayuscula

# Mayus = "que tal".upper() esto tambien funciona todo lo que esta dentro de las "comillas" lo devuelve en MAYUSCULAS

Minus = cadena1.lower() # Nos devuelve todo el string en minuscula

#Primera letra en mayuscula (convierte todo a minusculas y despues la primra letra la hace mayuscula)

prime_mayus = cadena2.capitalize()

#Encunetra la posicion de la letra, si no existe la letra devuelve -1

busqueda_find = cadena1.find("h")

#Buscamos una cadena en otra cadena INDEX, si no la encuntra tira error (excepción)

busqueda_index = cadena1.index("H")

#Si es un numero (en numero debe estar en forma de string) devuelve TRUE, sino nos devuelve FALSE : isnumeric()

es_numero = numero.isnumeric()

#Si es alfanumero nos devuelve TRUE, sino nos de vuelve FALSE : isalpha()

alpha_numertico = numerico.isalpha() #Cuenta nada más de la A-Z (no cuenta los espacio (porque es un caracter espacial))


#Cuenta la cantidad de veces que encuntra la letra en una cadena (si no esta la letra devuelve 0, porque no esta)
# también cuenta si busco una palabra, y detecta los espacio

encontrar_coicidencia = cadena1.count("Hola")


#Cantidad de caracteres que tiene un cadena (es una funcion) por eso se escribe antes de la variable (cuenta los espacio)
#Detecta numeros sin que estan en forma de string y si esta en forma de string también

cantidad_de_caracteres = len(numerico)


#verifica si una cadena empieza con otra cadena (palabra) , si es asi devuelve TRUE

empieza_con = cadena1.startswith("Hola")

#Verifica si la cadena termina con una cadena (palabra), si es asi nos devuelve TRUE

termina_con = cadena1.endswith("Alfredo")

#Si el valor 1, se encunetra en la cadena origienal. reemplza el valor 1 de la misma, por el valor que nosotros asignemos
# Si no esta el valor que queriamos reemplazer nos devuelve el valor original

cadena_nueva = cadena1.replace("Hola","Mucho gusto") #Reemplzamos

cadena_nueva2 = cadena_nueva.capitalize() #Convertimos en mayuscula la primera letra

#Separa cadenas con la cadena que le pasemos
#Crea una lista y separa las cadena (palabras)
#Si no encuntra la cadena(palabra) no devuelve un error []

cadena_separada = cadena1.split(",")

print (cadena_separada[1])


