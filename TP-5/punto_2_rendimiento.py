# =====================================================================
# TRABAJO PRÁCTICO 5: ANÁLISIS DE ALGORITMOS DE ORDENAMIENTO
# PUNTO 2: Medición y Análisis de Rendimiento
# Materia: Algoritmos y Estructuras / Programación Orientada a Objetos
# Alumno: Alfredo Patiño
# =====================================================================

import os
import gc
import time
import random
import psutil
import pandas as pd
from punto_1_algoritmos import bubble_sort, insertion_sort, merge_sort, quick_sort

def generar_datos(tamano=10000):
    """Genera listas con datos aleatorios, ordenados e inversos."""
    random.seed(42)
    return {
        "Aleatorio": [random.randint(1, tamano * 10) for _ in range(tamano)],
        "Ordenado": list(range(tamano)),
        "Inverso": list(range(tamano, 0, -1))
    }

def medir_rendimiento(algoritmo, datos):
    """
    Mide tiempo de ejecución con time.perf_counter() y memoria RAM con psutil.
    """
    proceso = psutil.Process(os.getpid())
    lista_copia = list(datos)
    
    gc.collect()
    memoria_inicio = proceso.memory_info().rss
    
    tiempo_inicio = time.perf_counter()
    resultado = algoritmo(lista_copia)
    tiempo_fin = time.perf_counter()
    
    memoria_fin = proceso.memory_info().rss
    
    tiempo_transcurrido = tiempo_fin - tiempo_inicio
    consumo_memoria_mb = max(0.0, (memoria_fin - memoria_inicio) / (1024 * 1024))
    
    return tiempo_transcurrido, consumo_memoria_mb, resultado

def main():
    tamano = 10000
    print(f"=== Mediciones del Punto 2 (N = {tamano:,}) ===")
    datos_dict = generar_datos(tamano)
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }
    
    resultados = []
    for tipo, lista in datos_dict.items():
        print(f"\nTipo de dato: {tipo}")
        for nombre, algo in algoritmos.items():
            t, m, _ = medir_rendimiento(algo, lista)
            print(f"  {nombre:15} -> Tiempo: {t:8.5f} s | RAM: {m:6.4f} MB")
            resultados.append({"Algoritmo": nombre, "Tipo de Dato": tipo, "Tiempo (s)": t, "Memoria (MB)": m})
            
    df = pd.DataFrame(resultados)
    print("\n=== RESUMEN TABULAR ===")
    print(df.to_string(index=False))
    return df

if __name__ == "__main__":
    main()
