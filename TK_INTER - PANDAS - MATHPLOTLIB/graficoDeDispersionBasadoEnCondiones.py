""" Ejercicio 3: Gráfico de Dispersión Basado en Condiciones
SCATTER PLOT Y FILTRADO CONDICIONAL DE DATOS
Se registraron 100 puntos de coordenadas aleatorias en un plano 2D para analizar la distribución de
valores de un sistema de prueba.
1. Genere 100 valores aleatorios para X y 100 para Y en el rango [0, 50].
2. Grafique los puntos en un gráfico de dispersión (scatter plot).
3. Pinte los puntos de color verde si su valor en Y es mayor o igual a 25, y de color rojo si es menor a
25.
4. Agregue título, etiquetas en los ejes (X, Y) y active la grilla. """


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# 1. Generar 100 valores aleatorios para X e Y en el rango [0, 50]
np.random.seed(24) # Semilla para reproducibilidad de los datos aleatorios
x = np.random.uniform(0, 50, 100)
y = np.random.uniform(0, 50, 100)

# 3. Aplicar filtrado condicional para los colores
# np.where evalúa la condición (y >= 25): si es True asigna 'green', si es False asigna 'red'
colores = np.where(y >= 25, 'green', 'red')

# 2. Creación del gráfico de dispersión
plt.figure(figsize=(9, 6))
plt.scatter(x, y, c=colores, alpha=0.8, edgecolors='black', s=50)

# 4. Formato visual: Título, etiquetas y grilla
plt.title('Distribución Espacial de Valores del Sistema de Prueba', fontsize=14, pad=15)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Creación de leyenda personalizada utilizando proxy artists para referenciar los colores
punto_verde = mlines.Line2D([], [], color='green', marker='o', linestyle='None', 
                            markersize=8, label='Y $\geq$ 25')
punto_rojo = mlines.Line2D([], [], color='red', marker='o', linestyle='None', 
                        markersize=8, label='Y < 25')
plt.legend(handles=[punto_verde, punto_rojo], loc='upper right', fontsize=10)

# Renderizado
plt.tight_layout()
plt.show()