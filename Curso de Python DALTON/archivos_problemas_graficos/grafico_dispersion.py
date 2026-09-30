#Importando las librerias necesarias
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

#importamdo el archivo
df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")

#print(df)

#Creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#Mostrando el grafico
plt.show()