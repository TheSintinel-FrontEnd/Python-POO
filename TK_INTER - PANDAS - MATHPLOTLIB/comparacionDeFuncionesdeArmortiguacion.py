""" Ejercicio 1: Comparación de Funciones de Amortiguación
VECTORES, OPERACIONES ELEMENTO A ELEMENTO Y CURVAS CRUZADAS
Una señal oscilatoria amortiguada se describe mediante la expresión matemática y(t) = e−a·t · cos(2π·f·t).
1. Genere un vector de tiempo t con 300 puntos equiespaciados en el intervalo [0, 5].
2. Grafique en una misma figura dos señales con frecuencia f = 2 Hz:
◦ Señal A (Amortiguación suave): a = 0.5 (línea continua azul).
◦ Señal B (Amortiguación fuerte): a = 1.8 (línea punteada roja).
3. Incluya leyenda, etiquetas en los ejes (t [s] e y(t)), título descriptivo y grilla de fondo. """


import numpy as np
import matplotlib.pyplot as plt

# 1. Generación del vector de tiempo 't'
# Utiliza linspace para crear 300 puntos equiespaciados en el intervalo cerrado [0, 5]
t = np.linspace(0, 5, 300)

# Parámetro de frecuencia (f) constante para ambas señales
f = 2  # Hz

# 2. Definición y cálculo de las señales
# Señal A (Amortiguación suave): a = 0.5
a_A = 0.5
y_A = np.exp(-a_A * t) * np.cos(2 * np.pi * f * t)

# Señal B (Amortiguación fuerte): a = 1.8
a_B = 1.8
y_B = np.exp(-a_B * t) * np.cos(2 * np.pi * f * t)

# 3. Creación y configuración del gráfico
plt.figure(figsize=(10, 6))

# Graficar Señal A (línea continua azul: 'b-')
plt.plot(t, y_A, 'b-', linewidth=2, label='Señal A: $a = 0.5$')

# Graficar Señal B (línea punteada roja: 'r--')
plt.plot(t, y_B, 'r--', linewidth=2, label='Señal B: $a = 1.8$')

# Formato visual: Título, etiquetas en los ejes y leyenda
plt.title('Comparación de Funciones de Amortiguación Oscilatoria', fontsize=14, pad=15)
plt.xlabel('t [s]', fontsize=12)
plt.ylabel('y(t)', fontsize=12)
plt.legend(loc='upper right', fontsize=11)

# Incorporación de la grilla de fondo
plt.grid(True, linestyle='--', alpha=0.7)

# Ajustar los márgenes para que no se corte ningún elemento
plt.tight_layout()

# Renderizar el gráfico en pantalla
plt.show()