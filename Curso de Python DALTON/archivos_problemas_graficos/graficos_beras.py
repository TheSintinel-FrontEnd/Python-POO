#Importando las librerias necesarias
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

#importamdo el archivo
df = pd.read_csv("archivos_problemas_graficos\\ingresos.csv")

#print(df)

#Creando el grafico
sns.barplot(x="fuente",y="ingreso",data=df)

#Obteniendo el total de los ingresos
total_ingreso = df["ingreso"].sum()

#Mostrando el total de los ingresos
print(total_ingreso)

#Mostrando el grafico
plt.show()