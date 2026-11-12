# =====================================================================
# TRABAJO PRÁCTICO 5: ANÁLISIS DE ALGORITMOS DE ORDENAMIENTO
# PUNTO 4: Aplicación a un Conjunto de Datos Real
# Materia: Algoritmos y Estructuras / Programación Orientada a Objetos
# Alumno: Alfredo Patiño
# =====================================================================

import os
import pandas as pd
from punto_1_algoritmos import quick_sort, merge_sort
from punto_2_rendimiento import medir_rendimiento

"""
===============================================================================
INFORME FINAL Y RESPUESTAS DEL TRABAJO PRÁCTICO 5
===============================================================================

1. ¿Cuál algoritmo fue el más rápido en promedio y por qué?
   Quick Sort fue el más rápido en promedio. Aunque tanto Quick Sort como
   Merge Sort poseen una complejidad teórica O(n log n), Quick Sort presenta
   factores constantes más reducidos en tiempo de CPU gracias a que realiza menos
   copias de arreglos y tiene un patrón de acceso a la memoria más favorable
   para la memoria caché del procesador.

2. ¿Cómo afectó el tipo de datos (ordenado, inverso, aleatorio) al rendimiento de cada algoritmo?
   - Bubble Sort e Insertion Sort demostraron un comportamiento lineal O(n) sumamente veloz
     cuando los datos ya estaban ordenados (gracias a la bandera swapped en Bubble Sort
     y a la condición de inserción directa). No obstante, en datos inversos y aleatorios
     su tiempo colapsó al orden cuadrático O(n^2), tardando más de 12 segundos.
   - Merge Sort mantuvo un tiempo constante de O(n log n) prácticamente indiferente
     al tipo de dato, pues la división recursiva y mezcla operan de la misma forma.
   - Quick Sort con pivote central (arr[len(arr) // 2]) resolvió eficientemente
     los tres casos en fracciones de milisegundo, previniendo el peor caso clásico O(n^2)
     que ocurre en datos ordenados cuando se eligen extremos como pivote.

3. ¿Qué algoritmo consideras el más eficiente para el uso general y por qué?
   Para uso general en memoria, Quick Sort es el más eficiente debido a su velocidad práctica.
   Sin embargo, si se requiere estabilidad (mantener el orden de elementos con claves iguales)
   o garantía matemática estricta contra el peor caso cuadrático, Merge Sort es la mejor opción.

4. ¿Qué observaste en el análisis con el archivo real (Demanda de celulares 2023.xlsx)?
   El archivo contiene 1,001 registros numéricos en la columna 'ganancia_neta'.
   Tanto Quick Sort como Merge Sort procesaron y ordenaron el dataset en un tiempo
   casi instantáneo (~0.002 a 0.003 segundos). A esta escala, la diferencia en tiempo
   es imperceptible para el usuario y el consumo de RAM fue de 0.00 MB a nivel de SO,
   lo que ratifica que para volúmenes estándar de datos ambos algoritmos son sumamente eficaces.
===============================================================================
"""

def analizar_archivo_real():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_excel = os.path.join(directorio_actual, "Demanda de celulares 2023.xlsx")
    
    print(f"Leyendo archivo: {ruta_excel}")
    df = pd.read_excel(ruta_excel)
    print(f"Dimensiones del dataset: {df.shape[0]} filas x {df.shape[1]} columnas")
    
    columna = "ganancia_neta"
    datos = df[columna].dropna().tolist()
    print(f"Columna seleccionada: '{columna}' ({len(datos)} registros)")
    
    # Medición de Quick Sort
    t_qs, m_qs, res_qs = medir_rendimiento(quick_sort, datos)
    print(f"\n[Quick Sort] Tiempo: {t_qs:.6f} s | Memoria: {m_qs:.4f} MB")
    
    # Medición de Merge Sort
    t_ms, m_ms, res_ms = medir_rendimiento(merge_sort, datos)
    print(f"[Merge Sort] Tiempo: {t_ms:.6f} s | Memoria: {m_ms:.4f} MB")
    
    assert res_qs == res_ms == sorted(datos), "Error en el ordenamiento"
    print("\n¡Ambos algoritmos ordenaron los datos reales con éxito!")

if __name__ == "__main__":
    analizar_archivo_real()
