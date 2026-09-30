
#Importando las librerias necesarias
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

#importamdo el archivo
df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")

#print(df)

#Creando el grafico
sns.boxplot(x="categorias",y="valor",data=df)


#Mostrando el grafico
plt.show()