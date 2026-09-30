""" Ejercicio 4: Visualización de Matriz de Sensores con Umbral
MATRICES 2D Y MAPAS DE CALOR (HEATMAPS)
Se desea representar visualmente la intensidad de una grilla bidimensional de sensores de 8 × 8.
1. Genere una matriz de tamaño 8 × 8 con números enteros aleatorios entre 0 y 100 (utilizando
np.random.randint ).
2. Muestre la matriz como una imagen con imshow utilizando la paleta de colores viridis .
3. Muestre la barra de color (colorbar) para identificar la escala de valores de intensidad.
4. Añada un título descriptivo y configure el gráfico para que se muestren claramente los índices de las
filas y columnas (del 0 al 7). """


import numpy as np
import matplotlib.pyplot as plt

# 1. Generación de la matriz 8x8 con enteros aleatorios entre 0 y 100
np.random.seed(33) # Semilla opcional para mantener la coherencia en las pruebas
# Se utiliza 101 como límite superior porque np.random.randint(low, high) no incluye el valor 'high'
matriz_sensores = np.random.randint(0, 101, size=(8, 8))

# Creación de la figura
plt.figure(figsize=(8, 6))

# 2. Visualización como mapa de calor usando la paleta 'viridis'
mapa_calor = plt.imshow(matriz_sensores, cmap='viridis')

# 3. Incorporación de la barra de color (colorbar)
plt.colorbar(mapa_calor, label='Nivel de Intensidad')

# 4. Configuración de título y etiquetas de los ejes
plt.title('Mapa de Calor: Matriz de Sensores', fontsize=14, pad=15)
plt.xlabel('Índice de Columna', fontsize=12)
plt.ylabel('Índice de Fila', fontsize=12)

# Forzar explícitamente que los "ticks" (marcas de los ejes) muestren los números del 0 al 7
plt.xticks(np.arange(8))
plt.yticks(np.arange(8))

# Ajuste visual para evitar recortes
plt.tight_layout()

# Renderizado final
plt.show()