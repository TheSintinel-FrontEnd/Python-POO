# =====================================================================
# TRABAJO PRÁCTICO 5: ANÁLISIS DE ALGORITMOS DE ORDENAMIENTO
# PUNTO 3: Visualización de Resultados con Matplotlib
# Materia: Algoritmos y Estructuras / Programación Orientada a Objetos
# Alumno: Alfredo Patiño
# =====================================================================

import os
import matplotlib.pyplot as plt
import numpy as np
from punto_2_rendimiento import main as obtener_resultados

def graficar_resultados(df_resultados):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    algoritmos = df_resultados["Algoritmo"].unique()
    tipos_datos = df_resultados["Tipo de Dato"].unique()
    
    x = np.arange(len(algoritmos))
    ancho = 0.25
    colores = {"Aleatorio": "#3498db", "Ordenado": "#2ecc71", "Inverso": "#e74c3c"}
    
    # 1. Gráfica de Tiempos
    plt.figure(figsize=(10, 6))
    for i, tipo in enumerate(tipos_datos):
        sub = df_resultados[df_resultados["Tipo de Dato"] == tipo]
        tiempos = sub["Tiempo (s)"].values
        plt.bar(x + (i - 1) * ancho, tiempos, width=ancho, label=tipo, color=colores[tipo], edgecolor="black", alpha=0.85)
        
    plt.title("Tiempo de Ejecución por Algoritmo y Tipo de Dato", fontsize=14, fontweight="bold")
    plt.xlabel("Algoritmo", fontsize=12)
    plt.ylabel("Tiempo (segundos)", fontsize=12)
    plt.xticks(x, algoritmos, fontsize=11)
    plt.legend(title="Tipo de Dato")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(directorio_actual, "grafico_tiempos_ejecucion.png"), dpi=300)
    
    # 2. Gráfica de Memoria
    plt.figure(figsize=(10, 6))
    for i, tipo in enumerate(tipos_datos):
        sub = df_resultados[df_resultados["Tipo de Dato"] == tipo]
        mem = sub["Memoria (MB)"].values
        plt.bar(x + (i - 1) * ancho, mem, width=ancho, label=tipo, color=colores[tipo], edgecolor="black", alpha=0.85)
        
    plt.title("Consumo de Memoria RAM por Algoritmo y Tipo de Dato", fontsize=14, fontweight="bold")
    plt.xlabel("Algoritmo", fontsize=12)
    plt.ylabel("Consumo RAM (MB)", fontsize=12)
    plt.xticks(x, algoritmos, fontsize=11)
    plt.legend(title="Tipo de Dato")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(directorio_actual, "grafico_consumo_memoria.png"), dpi=300)
    
    print("\n[OK] Gráficos guardados exitosamente como PNG.")
    try:
        plt.show()
    except Exception:
        pass

if __name__ == "__main__":
    df = obtener_resultados()
    graficar_resultados(df)
