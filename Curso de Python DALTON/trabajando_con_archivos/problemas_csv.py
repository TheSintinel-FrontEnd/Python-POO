import pandas as pd

df = pd.read_csv("trabajando_con_archivos\\texto.csv")

#convertir a string los datos de una columna

df ["edad"] = df["edad"].astype(str)

#Mostrando el camvio  de dato

#print(type(df["edad"][0]))

#Reemplazando los datos "correa" por "Fernandez"


# df["apellido"].replace("Patiño","Fernandez",inplace=True)

#Eliminando las filas sin datos
print(df)
df= df.dropna()
print(df)

#Eliminando las filas repetidas
print("------")
df = df.drop_duplicates()
print(df)


#Creando un archivo con el dataframe limpio

df.to_csv ("trabajando_con_archivos\\datos_limpios.csv")




