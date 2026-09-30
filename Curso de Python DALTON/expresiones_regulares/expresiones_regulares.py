
#Expresiones Regulares

#Importamos la funcion re
import re

texto = """Hola maestro, como estas es la 1. primera
Esta es la 22 segunda. linea
Esta es la 333 tercera."""

#Haceindo una busqueda simple
#resulrado = re.findall("Esta",texto,flags=re.IGNORECASE)


#\d busca diginos numero del 0-9
#resulrado1 = re.findall(r"\d",texto)


#\D busca todo menos diginos numero del 0-9
#resulrado2 = re.findall(r"\D",texto)

#\w busca carcateres alfanumericos [ a-z ] [ A-Z ] [ 0-9 ] [ _ ]
#resulrado3 = re.findall(r"\w",texto)

#\W busca todo menos carcateres alfanumericos [ a-z ] [ A-Z ] [ 0-9 ] [ _ ]
#resulrado4 = re.findall(r"\W",texto)

#\s busca espacion en blanco, espacios, saltos de linea
#resulrado5 = re.findall(r"\s",texto)

#\S busca todo menos espacion en blanco, saltos de linea
#resulrado6 = re.findall(r"\S",texto)

#. busca todo menos saltos de linea
#resultado7 = re.findall (r".",texto)


#\n para buscar unicamente saltos de linea
#resultado8 = re.findall(r"\n",texto)

#\ cancelando caracteres especial, cancelando la funcion del punto, y buscando puntos
#resultado9 = re.findall(r"\.",texto)

#Buscando en un cadena de caracteres, un numero,un punto y un espacio
#El patron que buscamos debe exitir, si no, no devulve nada []
#resultado10 = re.findall(f"\d\.\s",texto)

#Buscando el principio de una linea
# ^ busca el comienzo de una linea
#[flags=re.M] activa la multilinea

resulto= re.findall(f"^Hola",texto,)

#$ Busca el final de una linea

resultado11 = re.findall  (f"tercera.$",texto,flags=re.M)

#(n) busca n cantidades de veces el valor de la izquierda
#No distingue agrupaciones de numeros entre "333" y "22", 

resultado12 = re.findall(r"\d{1}\s",texto)

#{n,m} al menos n,como maximo m

resultado13 = re.findall(r"\d{2,3}",texto)


# | bucsa uns cosa o la otra
resultado14 = re.findall(r"\d{2,3}|Hola",texto)

print(resultado14)
