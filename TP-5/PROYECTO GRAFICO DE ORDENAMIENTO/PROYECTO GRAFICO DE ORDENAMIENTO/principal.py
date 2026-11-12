import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import random
import time
import matplotlib.pyplot as plt

# =============================================================================
# Módulo de Algoritmos de Ordenamiento
# =============================================================================

def mergesort(lista):
    """Implementación recursiva del algoritmo Mergesort."""
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    lista_izquierda = mergesort(lista[:mitad])
    lista_derecha = mergesort(lista[mitad:])
    
    return mezclar(lista_izquierda, lista_derecha)

def mezclar(lista_izquierda, lista_derecha):
    """Función auxiliar para mezclar dos listas ordenadas."""
    lista_ordenada = []
    i = j = 0
    
    while i < len(lista_izquierda) and j < len(lista_derecha):
        if lista_izquierda[i] < lista_derecha[j]:
            lista_ordenada.append(lista_izquierda[i])
            i += 1
        else:
            lista_ordenada.append(lista_derecha[j])
            j += 1
    
    lista_ordenada.extend(lista_izquierda[i:])
    lista_ordenada.extend(lista_derecha[j:])
        
    return lista_ordenada

def quicksort_in_place(arr, bajo, alto):
    """Implementación recursiva del algoritmo Quicksort (in-place)."""
    if bajo < alto:
        indice_pivote = particion(arr, bajo, alto)
        quicksort_in_place(arr, bajo, indice_pivote - 1)
        quicksort_in_place(arr, indice_pivote + 1, alto)

def particion(arr, bajo, alto):
    """Función auxiliar para particionar la lista alrededor de un pivote."""
    pivote = arr[alto]
    i = bajo - 1
    
    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1



# =============================================================================
# Módulo de Carga de Datos
# =============================================================================

def cargar_csv(ruta_archivo):
    """Lee datos de un archivo CSV y devuelve la primera columna como lista."""
    try:
        df = pd.read_csv(ruta_archivo)
        return df.iloc[:, 0].tolist()
    except Exception as e:
        messagebox.showerror("Error de Carga", f"Error al leer el archivo CSV: {e}")
        return None

def cargar_excel(ruta_archivo):
    """Lee datos de un archivo Excel y devuelve la primera columna como lista."""
    try:
        df = pd.read_excel(ruta_archivo)
        return df.iloc[:, 0].tolist()
    except Exception as e:
        messagebox.showerror("Error de Carga", f"Error al leer el archivo Excel: {e}")
        return None

def generar_datos_aleatorios(cantidad, rango_min, rango_max):
    """Genera una lista de números enteros aleatorios."""
    return [random.randint(rango_min, rango_max) for _ in range(cantidad)]

# =============================================================================
# Módulo de Benchmarking y Gráficos
# =============================================================================

def ejecutar_benchmark(algoritmo, datos):
    """Ejecuta un algoritmo de ordenamiento y mide su tiempo."""
    lista_copia = list(datos)
    tiempo_inicio = time.perf_counter()
    
    # Manejar las llamadas a los algoritmos según su tipo de implementación
    if algoritmo == quicksort_in_place:
        algoritmo(lista_copia, 0, len(lista_copia) - 1)
    else:
        algoritmo(lista_copia)
        
    tiempo_fin = time.perf_counter()
    return tiempo_fin - tiempo_inicio

def comparar_algoritmos(tamaños_lista, num_pruebas=5):
    """Compara Quicksort y Mergesort midiendo su tiempo de ejecución."""
    tiempos_quicksort = []
    tiempos_mergesort = []

    for tamaño in tamaños_lista:
        tiempo_total_qs = 0
        tiempo_total_ms = 0
        
        for _ in range(num_pruebas):
            datos_aleatorios = generar_datos_aleatorios(tamaño, 0, tamaño * 10)
            tiempo_total_qs += ejecutar_benchmark(quicksort_in_place, datos_aleatorios)
            tiempo_total_ms += ejecutar_benchmark(mergesort, datos_aleatorios)
            
        tiempos_quicksort.append(tiempo_total_qs / num_pruebas)
        tiempos_mergesort.append(tiempo_total_ms / num_pruebas)
        
    return tiempos_quicksort, tiempos_mergesort

def graficar_tiempos(tamaños_lista, tiempos_quicksort, tiempos_mergesort):
    """Genera un gráfico comparando los tiempos de Quicksort y Mergesort."""
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños_lista, tiempos_quicksort, label='Quicksort', marker='o')
    plt.plot(tamaños_lista, tiempos_mergesort, label='Mergesort', marker='x')
    
    plt.xlabel('Tamaño de la Lista')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Comparación de Tiempo de Ejecución: Quicksort vs Mergesort')
    plt.legend()
    plt.grid(True)
    plt.show()

# =============================================================================
# Lógica de la Interfaz Gráfica (Tkinter)
# =============================================================================

class AppOrdenamiento:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmos de Ordenamiento y Comparación")
        self.datos = []
        
        self.setup_ui()
    
    def setup_ui(self):
        # Frame para la carga de datos
        frame_carga = tk.Frame(self.root)
        frame_carga.pack(pady=10)
        
        tk.Label(frame_carga, text="Cargar datos desde:").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_carga, text="CSV", command=self.cargar_datos_csv).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_carga, text="Excel", command=self.cargar_datos_excel).pack(side=tk.LEFT, padx=5)
        
        tk.Label(frame_carga, text="Generar datos aleatorios:").pack(side=tk.LEFT, padx=10)
        tk.Label(frame_carga, text="Cantidad:").pack(side=tk.LEFT, padx=5)
        self.entry_random = tk.Entry(frame_carga, width=10)
        self.entry_random.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_carga, text="Generar", command=self.generar_datos).pack(side=tk.LEFT, padx=5)
        
        # Frame para los botones de ordenamiento y comparación
        frame_ordenamiento = tk.Frame(self.root)
        frame_ordenamiento.pack(pady=10)
        
        tk.Button(frame_ordenamiento, text="Ordenar con Quicksort", command=self.ejecutar_quicksort).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_ordenamiento, text="Ordenar con Mergesort", command=self.ejecutar_mergesort).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_ordenamiento, text="Comparar Algoritmos", command=self.ejecutar_comparacion).pack(side=tk.LEFT, padx=10)
        
        # Etiqueta para mostrar los resultados
        self.label_resultado = tk.Label(self.root, text="No hay datos cargados.", justify=tk.LEFT)
        self.label_resultado.pack(pady=20)

# Botón para salir
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

    def cargar_datos_csv(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if archivo:
            self.datos = cargar_csv(archivo)
            if self.datos is not None:
                self.actualizar_display()
            
    def cargar_datos_excel(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
        if archivo:
            self.datos = cargar_excel(archivo)
            if self.datos is not None:
                self.actualizar_display()

    def generar_datos(self):
        try:
            cantidad = int(self.entry_random.get())
            self.datos = generar_datos_aleatorios(cantidad, 1, 1000)
            self.actualizar_display()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
            
    def ejecutar_quicksort(self):
        if not self.datos:
            messagebox.showwarning("Advertencia", "No hay datos para ordenar.")
            return
        
        datos_copia = self.datos[:]
        quicksort_in_place(datos_copia, 0, len(datos_copia) - 1)
        self.actualizar_display(datos_copia)
        
    def ejecutar_mergesort(self):
        if not self.datos:
            messagebox.showwarning("Advertencia", "No hay datos para ordenar.")
            return
            
        datos_ordenados = mergesort(self.datos[:])
        self.actualizar_display(datos_ordenados)
        
    def ejecutar_comparacion(self):
        tamaños = [100, 500, 1000, 2000, 5000, 10000]
        num_pruebas = 5

        messagebox.showinfo("Comparación", "Iniciando la comparación de algoritmos. Esto puede tomar un momento...")
        
        tiempos_qs, tiempos_ms = comparar_algoritmos(tamaños, num_pruebas)
        
        graficar_tiempos(tamaños, tiempos_qs, tiempos_ms)
        messagebox.showinfo("Comparación Completada", "Se ha generado el gráfico de comparación.")
        
    def actualizar_display(self, datos_ordenados=None):
        if not self.datos:
            self.label_resultado.config(text="No hay datos cargados.")
            return
            
        texto_original = f"Lista cargada ({len(self.datos)} elementos): {self.datos[:10]}..."
        if datos_ordenados:
            texto_ordenado = f"Lista ordenada ({len(datos_ordenados)} elementos): {datos_ordenados[:10]}..."
        else:
            texto_ordenado = "Lista ordenada: []"
            
        self.label_resultado.config(text=f"{texto_original}\n{texto_ordenado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppOrdenamiento(root)
    root.mainloop()