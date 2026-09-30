""" Ejercicio 2: Análisis Estadístico de Mediciones Industriales
DISTRIBUCIÓN NORMAL, HISTOGRAMAS Y LÍMITES DE TOLERANCIA
Un sensor de temperatura registra mediciones en una planta industrial. El valor nominal esperado es de
25 °C, con un ruido estocástico asociado a la precisión del instrumento.
1. Simule 2000 lecturas del sensor generando una distribución normal con media μ = 25 y desviación
estándar σ = 1.5.
2. Grafique el histograma de las mediciones utilizando 40 intervalos (bins).
3. Dibuje dos líneas verticales discontinuas en los límites de tolerancia aceptables: 22 °C (Límite
Inferior) y 28 °C (Límite Superior) de color rojo.
4. Muestre en la leyenda el porcentaje de mediciones que cayeron dentro del rango de tolerancia [22,
28] (calcule dicho valor utilizando funciones de numpy ). """

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
media_mu = 25
desviacion_sigma = 1.5
num_lecturas = 2000

# 1. Simulación de las lecturas del sensor (Distribución Normal)
np.random.seed(42) # Fijamos la semilla para que los resultados sean reproducibles
mediciones = np.random.normal(media_mu, desviacion_sigma, num_lecturas)

# Definición de los límites de tolerancia
limite_inferior = 22
limite_superior = 28

# 4. Cálculo del porcentaje de mediciones dentro de la tolerancia
# Usamos np.logical_and para encontrar los valores que cumplen ambas condiciones
dentro_tolerancia = np.logical_and(mediciones >= limite_inferior, mediciones <= limite_superior)
# Sumamos la cantidad de valores 'True' y calculamos el porcentaje
porcentaje_dentro = (np.sum(dentro_tolerancia) / num_lecturas) * 100

# 2 y 3. Creación y configuración del gráfico
plt.figure(figsize=(10, 6))

# Graficar el histograma con 40 intervalos (bins)
plt.hist(mediciones, bins=40, color='skyblue', edgecolor='black', alpha=0.7, 
        label=f'Mediciones\nDentro de tol.: {porcentaje_dentro:.1f}%')

# 3. Dibujar las líneas verticales de los límites de tolerancia (rojas, discontinuas)
plt.axvline(x=limite_inferior, color='red', linestyle='--', linewidth=2, label='Límite Inferior (22°C)')
plt.axvline(x=limite_superior, color='red', linestyle='--', linewidth=2, label='Límite Superior (28°C)')

# Formato visual
plt.title('Distribución de Mediciones de Temperatura', fontsize=14, pad=15)
plt.xlabel('Temperatura [°C]', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.legend(loc='upper right', fontsize=10)

# Incorporación de la grilla
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ajuste y renderizado
plt.tight_layout()
plt.show()