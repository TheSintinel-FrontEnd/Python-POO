
#Con el import (impotamos) el modulo de la misma carpeta (modulo_saludar)

# Y con el "as" asignamos "modulo_saludar" a "msaludar"

#import modulo_saludar as msaludar
#desde ese modulo, importamos las 2 funciones

#Llamo a la carpta donde esta el modulo, y depues llamo al modulo
from CARPETA_DEL_MODULO_SALUDAR.modulo_saludar import saludar as saludar_nomral ,saludar_raro as saludar_como_coscu


# Creamos la variable saludar, la igualamos a "msaludar", ponemos su extencion "saludar" 
# Y lo que esta entre ("esto es el valor") se lo enviamos al modulo 
#saludo = msaludar("Alfredo")

#Creamos las variables igualamos a la funcion y le pasamos entre ("name")
saludo = saludar_nomral("Alfredo")
saludo_raro = saludar_como_coscu("jeo")

#Mostramos los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namesapce

#print(dir(m_saludar))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado

#print(m_saludar.__name__)