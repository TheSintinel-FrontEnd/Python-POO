# =====================================================================
# Trabajo Practico 5: Analisis de Algoritmos de Ordenamiento
# Materia: Algoritmos y Estructuras / POO
# Alumno: Alfredo Patiño
# =====================================================================

import os
import time
import random
import psutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ------------------------------------------------------------------
# PUNTO 1: Implementacion de los Algoritmos de Ordenamiento
# ------------------------------------------------------------------

# 1. Ordenamiento Burbuja (Bubble Sort)
def bubble_sort(arr):
    # Copiamos la lista para no modificar la original
    lista = list(arr)
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        # Si no hubo intercambios en esta pasada, la lista ya esta ordenada
        if not intercambio:
            break
    return lista


# 2. Ordenamiento por Insercion (Insertion Sort)
def insertion_sort(arr):
    lista = list(arr)
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # Desplazamos los elementos que sean mayores que el actual hacia adelante
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


# 3. Ordenamiento por Mezcla (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    
    mitad = len(arr) // 2
    izquierda = merge_sort(arr[:mitad])
    derecha = merge_sort(arr[mitad:])
    
    return mezclar(izquierda, derecha)


def mezclar(izq, der):
    # Junta las dos sublistas ya ordenadas en una sola
    resultado = []
    i = 0
    j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    # Agregamos los que sobren
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


# 4. Ordenamiento Rapido (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    
    # Tomamos el elemento del medio como pivote para que no falle con listas ya ordenadas
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    return quick_sort(menores) + iguales + quick_sort(mayores)


# ------------------------------------------------------------------
# PUNTO 2: Analisis del Rendimiento con Diferentes Tipos de Datos
# ------------------------------------------------------------------

# 1. Funcion para generar las listas pedidas
def generar_datos(tamano=10000):
    # Semilla para que los numeros sean repetibles en las pruebas
    random.seed(42)
    datos_aleatorios = [random.randint(1, tamano * 5) for _ in range(tamano)]
    datos_ordenados = list(range(tamano))
    datos_inversos = list(range(tamano, 0, -1))
    
    return {
        "Aleatorio": datos_aleatorios,
        "Ordenado": datos_ordenados,
        "Inverso": datos_inversos
    }


# 2. Funcion de Medicion (mide tiempo y memoria RAM con psutil)
def medir_rendimiento(algoritmo, datos):
    proceso = psutil.Process(os.getpid())
    lista_copia = list(datos)
    
    # Tomamos la memoria antes de arrancar
    memoria_inicio = proceso.memory_info().rss
    
    # Medimos el tiempo que tarda
    tiempo_inicio = time.perf_counter()
    resultado = algoritmo(lista_copia)
    tiempo_fin = time.perf_counter()
    
    memoria_fin = proceso.memory_info().rss
    
    tiempo_total = tiempo_fin - tiempo_inicio
    # Pasamos los bytes a Megabytes (MB)
    memoria_mb = max(0.0, (memoria_fin - memoria_inicio) / (1024 * 1024))
    
    return tiempo_total, memoria_mb, resultado


# 3. Ejecucion y recopilacion de resultados
def ejecutar_pruebas_rendimiento(tamano=10000):
    print(f"\n--- Iniciando mediciones con listas de {tamano:,} elementos ---")
    listas = generar_datos(tamano)
    
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }
    
    resultados = {}
    
    for tipo, datos in listas.items():
        print(f"\nProbando listas tipo: [{tipo}]")
        resultados[tipo] = {}
        for nombre, funcion in algoritmos.items():
            print(f" -> Ejecutando {nombre}...", end=" ", flush=True)
            t, m, _ = medir_rendimiento(funcion, datos)
            print(f"Termino en {t:.5f} seg | Memoria: {m:.4f} MB")
            resultados[tipo][nombre] = {"tiempo": t, "memoria": m}
            
    # Mostramos los resultados en una tablita por consola
    print("\n" + "=" * 58)
    print(f"{'Algoritmo':15} | {'Tipo de Dato':12} | {'Tiempo (s)':12} | {'Memoria (MB)':12}")
    print("=" * 58)
    for tipo in resultados:
        for nombre in resultados[tipo]:
            t = resultados[tipo][nombre]["tiempo"]
            m = resultados[tipo][nombre]["memoria"]
            print(f"{nombre:15} | {tipo:12} | {t:10.5f} s | {m:10.4f} MB")
    print("=" * 58)
    
    return resultados


# ------------------------------------------------------------------
# PUNTO 3: Visualizacion de Resultados con Matplotlib
# ------------------------------------------------------------------

def graficar_resultados(resultados):
    algoritmos = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
    tipos = ["Aleatorio", "Ordenado", "Inverso"]
    colores = ["#3498db", "#2ecc71", "#e74c3c"]
    
    x = np.arange(len(algoritmos))
    ancho = 0.25
    
    # 1. Grafico de Tiempos de ejecucion
    plt.figure(figsize=(9, 5))
    for i, tipo in enumerate(tipos):
        tiempos = [resultados[tipo][algo]["tiempo"] for algo in algoritmos]
        plt.bar(x + (i - 1) * ancho, tiempos, width=ancho, label=tipo, color=colores[i], edgecolor="black")
        
    plt.title("Tiempo de Ejecucion por Algoritmo y Tipo de Dato")
    plt.xlabel("Algoritmos")
    plt.ylabel("Tiempo (segundos)")
    plt.xticks(x, algoritmos)
    plt.legend(title="Tipo de dato")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("grafico_tiempos_ejecucion.png")
    print("Grafico guardado: 'grafico_tiempos_ejecucion.png'")
    
    # 2. Grafico de Consumo de Memoria RAM
    plt.figure(figsize=(9, 5))
    for i, tipo in enumerate(tipos):
        memorias = [resultados[tipo][algo]["memoria"] for algo in algoritmos]
        plt.bar(x + (i - 1) * ancho, memorias, width=ancho, label=tipo, color=colores[i], edgecolor="black")
        
    plt.title("Consumo de Memoria RAM por Algoritmo y Tipo de Dato")
    plt.xlabel("Algoritmos")
    plt.ylabel("Memoria RAM (MB)")
    plt.xticks(x, algoritmos)
    plt.legend(title="Tipo de dato")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("grafico_consumo_memoria.png")
    print("Grafico guardado: 'grafico_consumo_memoria.png'")
    
    try:
        plt.show()
    except Exception:
        pass


# ------------------------------------------------------------------
# PUNTO 4: Aplicacion a un Conjunto de Datos Real
# ------------------------------------------------------------------

def analizar_archivo_real():
    # Buscamos el archivo en la misma carpeta del script
    directorio = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio, "Demanda de celulares 2023.xlsx")
    
    print(f"\n--- Punto 4: Analisis con archivo real ---")
    print(f"Cargando archivo: Demanda de celulares 2023.xlsx")
    df = pd.read_excel(ruta_archivo)
    print(f"Filas leidas: {len(df)}")
    
    # Seleccionamos la columna de ganancias netas
    columna = "ganancia_neta"
    datos_columna = df[columna].dropna().tolist()
    print(f"Columna seleccionada: '{columna}' ({len(datos_columna)} elementos)")
    
    # Medimos Quick Sort
    t_qs, m_qs, res_qs = medir_rendimiento(quick_sort, datos_columna)
    print(f"\nQuick Sort -> Tiempo: {t_qs:.6f} segundos | Memoria: {m_qs:.4f} MB")
    
    # Medimos Merge Sort
    t_ms, m_ms, res_ms = medir_rendimiento(merge_sort, datos_columna)
    print(f"Merge Sort -> Tiempo: {t_ms:.6f} segundos | Memoria: {m_ms:.4f} MB")
    
    if t_qs < t_ms:
        print("\n=> Quick Sort fue mas rapido que Merge Sort en el archivo real.")
    else:
        print("\n=> Merge Sort fue mas rapido que Quick Sort en el archivo real.")


# ------------------------------------------------------------------
# INFORME FINAL / CONCLUSIONES (Punto 4.4)
# ------------------------------------------------------------------
"""
===============================================================================
INFORME FINAL Y RESPUESTAS DEL TRABAJO PRACTICO 5
===============================================================================

1. ¿Cual algoritmo fue el mas rapido en promedio y por que?
   El mas rapido en promedio fue Quick Sort, seguido de cerca por Merge Sort.
   Ambos tienen una complejidad teorica de O(n log n), pero Quick Sort es mas
   rapido en la practica porque hace operaciones mas directas en memoria y no tiene
   que estar creando tantas sublistas nuevas como hace Merge Sort al dividir y mezclar.

2. ¿Como afecto el tipo de datos (ordenado, inverso, aleatorio) al rendimiento de cada algoritmo?
   - En Bubble Sort e Insertion Sort el cambio fue tremendo: cuando la lista ya estaba ordenada
     tardaron apenas 0.001 segundos porque la bandera de intercambio (en Bubble) o el while (en Insertion)
     hacen que terminen en una sola pasada lineal O(n). Pero cuando la lista venia en orden inverso
     o aleatoria, tardaron muchisimo (entre 3 y 12 segundos) porque tuvieron que hacer todas las
     comparaciones posibles (complejidad O(n^2)).
   - En Merge Sort el tiempo fue casi parejo en los tres casos (alrededor de 0.03 segundos) porque
     no le importa el orden previo: siempre divide la lista al medio y la vuelve a mezclar de la misma forma.
   - En Quick Sort funciono muy rapido en todos los casos porque tomamos como pivote el elemento del centro.
     Si hubieramos tomado el primer elemento, con la lista ya ordenada se habria vuelto O(n^2) y habria
     dado error de recursion en Python.

3. ¿Que algoritmo consideras el mas eficiente para el uso general y por que?
   Para uso general considero que Quick Sort es el mas eficiente porque es el mas rapido en la mayoria
   de situaciones reales y no consume tanta memoria extra. Sin embargo, si importara mucho que los
   elementos iguales mantengan su orden original (algoritmo estable), o si tuviera que ordenar datos
   en un archivo muy grande, Merge Sort seria una opcion mas segura.

4. ¿Que observaste en el analisis con el archivo real (Demanda de celulares 2023.xlsx)?
   El archivo tiene 1001 filas y use la columna 'ganancia_neta'. Como son apenas 1001 numeros,
   tanto Quick Sort como Merge Sort tardaron menos de 0.003 segundos (casi nada). En conjuntos de datos
   de este tamaño la diferencia no se nota para el usuario y el consumo de RAM dio 0.00 MB porque entra
   sobrado en la memoria del programa.
===============================================================================
"""

if __name__ == "__main__":
    print("=" * 60)
    print("  TRABAJO PRACTICO 5: ALGORITMOS DE ORDENAMIENTO")
    print("  Alumno: Alfredo Patiño")
    print("=" * 60)
    
    # 1. Ejecutamos las pruebas con 10,000 elementos (Punto 2)
    resultados = ejecutar_pruebas_rendimiento(tamano=10000)
    
    # 2. Generamos los graficos con matplotlib (Punto 3)
    graficar_resultados(resultados)
    
    # 3. Analizamos el Excel con datos reales (Punto 4)
    analizar_archivo_real()
