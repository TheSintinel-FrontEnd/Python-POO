
#Importando el pandas

import pandas as pd

# print(type(pd)) imprimiendo la clase en este caso "module" o "modulo"

#Usamos la funcion read.csv para leer el archivo CSV
df = pd.read_csv("archivo\\texto.csv",encoding="UTF-8")
df2 = pd.read_csv("archivo\\texto.csv",encoding="UTF-8")

#df = data freame (conceptualmente)

#Obteniendo los datos de la columna nombre
#print(df["nombre"])

#Creamos una cadena de numeros
cadena = "012345678910"
#Imprimimos la cadena pero mostrara desde un punto inical hasta uno final (si incluira el inicio, pero no el final)
#ejemplo si es del 2 hasta el 9 , incluira al 2 pero al recorrerlo no mostrara el 9 sino el 8
#print(cadena[2:9]) #desde el 2 hasta el 8, esto se llama slicing 

#ordenamos el datafreme por las edades de forma ascendente
# df_orden_ascendente = df.sort_values("edad")

#Ordenamos el datafreme por las edades de forma descendente
#df_orden_descendente = df.sort_values("edad",ascending=False)

#print(df_orden_descendente)



def Descendente (df):
    
    dataframe1 = df
    
    dataframe_ascen = dataframe1.sort_values("edad")
    
    return f"Orden descendente menor a mayor: \n{dataframe_ascen}"




def Ascent (df):
    
    dataframe2 = df
    
    asec = dataframe2.sort_values("edad",ascending=False)
    return f"Orden ascendente de mayor a menor: \n{asec}"


d_o_des = Descendente(df)

d_o_asc =Ascent(df)

print(d_o_des)
print("-----------------------")
print(d_o_asc)

#Concatenando los 2 DataFrame

df_concatenado = pd.concat([df,df2])

print(df_concatenado)

#accediendo a la primera fila con head()
print("\n")

primeras_filas = df.head(1)
#print(primeras_filas)


#accediendo a las ultimas filas con tail()

ultimas_filas = df.tail(2)

#print(ultimas_filas)

#accediendo a la cantidad de filas y clumnas con shape

filas_y_columnas_totales = df.shape
#desempaquedo
# filas_totales,columnas_totales = df.shape
#print(filas_y_columnas_totales)

#obteniendo data estadistica del dataframe
df_info = df.describe()
#print(df_info)


#accediendo a la edad de la fila 2

elemento_espesifico_loc = df.loc[2,"edad"]
#print(elemento_espesifico_loc)

#accediendo a la edad de la fila 2

elemento_espesifico_iloc = df.iloc[2,2]
#print(elemento_espesifico_iloc)

#accediendo a todos los datos con iloc
nombres = df.iloc[:,0]
apellidos = df.iloc[:,1]
edad = df.iloc[:,2]

#print(apellidos)

#accediendo a todos los datos en fila con loc

fila_csv = df.loc[0,:]

print(fila_csv)

mayor_que_18 = df.loc[df["edad"]>18,:]

print(mayor_que_18)


