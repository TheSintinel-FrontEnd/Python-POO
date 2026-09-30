#Si la carpeta estuviera en la misma ruta se usario lo de abajo
#import  Funciones_buenas.saludar as m_saludar

import sys

#print(m_saludar.saludar("Lucas"))

import sys

sys.path.append("C:\\Users\\af449\\Desktop\\Curso de Python DALTON\\Funciones_buenas")

print(sys.path)

import saludar as m_saludo

print(m_saludo.saludar("Alfredo"))
