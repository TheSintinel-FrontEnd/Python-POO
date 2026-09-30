#Importando las librerias necesarias
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

#importamdo el archivo
df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")

#print(df)

#Creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)


#Creando un punto en el momento de más pedos
plt.plot("01-08",17,"o")

#Mostrando el grafico
plt.show()
