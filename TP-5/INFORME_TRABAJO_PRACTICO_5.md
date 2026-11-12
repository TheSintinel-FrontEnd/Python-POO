# TRABAJO PRÁCTICO N° 5: ANÁLISIS DE ALGORITMOS DE ORDENAMIENTO

**Materia:** Algoritmos y Estructuras de Datos / Programación Orientada a Objetos  
**Alumno:** Alfredo Patiño  
**Profesor:** Cadamuro  
**Fecha:** Noviembre 2026  

---

## 1. Objetivos del Trabajo Práctico
* Comprender el funcionamiento, ventajas y desventajas de algoritmos de ordenamiento cuadráticos ($O(n^2)$) y logarítmicos ($O(n \log n)$).
* Medir experimentalmente el **tiempo de ejecución** y el **consumo de memoria RAM** utilizando librerías estándar y de monitoreo de sistema (`time` y `psutil`).
* Estudiar el impacto del orden inicial de los datos (aleatorio, ordenado, inverso) en cada algoritmo.
* Aplicar los algoritmos a un conjunto de datos real provisto por la cátedra (`Demanda de celulares 2023.xlsx`) mediante `pandas`.
* Generar visualizaciones gráficas comparativas claras con `matplotlib`.

---

## 2. Punto 1: Implementación de Algoritmos de Ordenamiento

Se implementaron en Python las cuatro funciones requeridas, asegurando modularidad, legibilidad y el manejo seguro de los datos mediante copias para evitar efectos colaterales.

### 2.1. Ordenamiento Burbuja (`bubble_sort`)
* **Mecanismo:** Recorre la lista de forma iterativa, comparando elementos adyacentes e intercambiándolos si están desordenados.
* **Optimización implementada:** Se incluyó una bandera booleana (`swapped`/`intercambio`) que detecta si en una pasada completa no se produjo ningún intercambio; si es así, finaliza de inmediato. Esto reduce su complejidad en listas ya ordenadas a $O(n)$.
* **Complejidad:**
  * Mejor caso: $O(n)$
  * Caso promedio y peor caso: $O(n^2)$
  * Memoria auxiliar: $O(1)$

### 2.2. Ordenamiento por Inserción (`insertion_sort`)
* **Mecanismo:** Construye el arreglo ordenado elemento por elemento. Toma el elemento actual (clave) y lo desplaza hacia la izquierda hasta encontrar su ubicación adecuada.
* **Complejidad:**
  * Mejor caso: $O(n)$ (si la lista ya viene ordenada)
  * Caso promedio y peor caso: $O(n^2)$
  * Memoria auxiliar: $O(1)$

### 2.3. Ordenamiento por Mezcla (`merge_sort`)
* **Mecanismo:** Aplica la estrategia de **Divide y Vencerás**. Divide recursivamente la lista por la mitad hasta llegar a sublistas unitarias y luego las fusiona ordenadamente mediante una función auxiliar `_mezclar`.
* **Complejidad:**
  * Todos los casos (mejor, promedio y peor): $O(n \log n)$
  * Memoria auxiliar: $O(n)$ debido a las sublistas temporales creadas durante la división y mezcla.

### 2.4. Ordenamiento Rápido (`quick_sort`)
* **Mecanismo:** Aplica **Divide y Vencerás**. Elige un pivote y clasifica los elementos en menores, iguales y mayores, concatenando recursivamente los resultados.
* **Técnica de selección de pivote:** Se utilizó el **elemento central** (`pivote = arr[len(arr) // 2]`). Esta elección es crucial en la práctica, pues previene que listas ya ordenadas o inversas degeneren en el peor caso cuadrático $O(n^2)$ y evita errores de desbordamiento de pila de recursión (`RecursionError`).
* **Complejidad:**
  * Mejor y promedio: $O(n \log n)$
  * Peor caso teórico: $O(n^2)$ (si el pivote fuese siempre el mínimo o máximo)
  * Memoria auxiliar: $O(n)$ en implementación funcional.

---

## 3. Punto 2: Medición y Análisis de Rendimiento

### 3.1. Metodología de Medición
1. **Generación de datos:** Se creó la función `generar_datos(tamano=10000)` que construye tres listas de 10,000 elementos:
   * **Aleatorio:** Valores enteros pseudoaleatorios entre 1 y 100,000 (semilla fijada en 42 para reproducibilidad).
   * **Ordenado:** Secuencia creciente del 0 al 9,999.
   * **Inverso:** Secuencia decreciente del 10,000 al 1.
2. **Función de medición:** `medir_rendimiento(algoritmo, datos)`:
   * **Tiempo:** Utiliza `time.perf_counter()` para alta resolución (nanosegundos).
   * **Memoria:** Monitorea la memoria RAM a nivel de proceso (`psutil.Process(os.getpid()).memory_info().rss`), forzando una recolección de basura previa (`gc.collect()`) para registrar el delta neto en Megabytes (MB).

### 3.2. Tabla de Resultados Experimentales ($N = 10,000$ elementos)

| Algoritmo | Tipo de Dato | Tiempo de Ejecución (s) | Consumo de RAM (MB) | Complejidad Observada |
| :--- | :--- | :---: | :---: | :---: |
| **Bubble Sort** | Aleatorio | 9.1082 s | 0.0742 MB | $O(n^2)$ |
| **Bubble Sort** | Ordenado | **0.0011 s** | 0.0039 MB | $O(n)$ (Optimizado) |
| **Bubble Sort** | Inverso | **12.7930 s** | 0.0000 MB | $O(n^2)$ (Peor caso) |
| **Insertion Sort** | Aleatorio | 3.6227 s | 0.0781 MB | $O(n^2)$ |
| **Insertion Sort** | Ordenado | **0.0018 s** | 0.0000 MB | $O(n)$ |
| **Insertion Sort** | Inverso | **6.9469 s** | 0.0352 MB | $O(n^2)$ (Peor caso) |
| **Merge Sort** | Aleatorio | 0.0449 s | 0.3164 MB | $O(n \log n)$ |
| **Merge Sort** | Ordenado | 0.0296 s | 0.1094 MB | $O(n \log n)$ |
| **Merge Sort** | Inverso | 0.0286 s | 0.0508 MB | $O(n \log n)$ (Consistente) |
| **Quick Sort** | Aleatorio | **0.0326 s** | 0.1406 MB | $O(n \log n)$ (Más rápido) |
| **Quick Sort** | Ordenado | **0.0204 s** | 0.0312 MB | $O(n \log n)$ |
| **Quick Sort** | Inverso | **0.0199 s** | 0.0273 MB | $O(n \log n)$ |

---

## 4. Punto 3: Visualización de Resultados

Se desarrollaron gráficos de barras con `matplotlib` guardados en alta resolución (300 DPI):

1. **`grafico_tiempos_ejecucion.png`**: Compara el tiempo en segundos en escala directa, destacando visualmente la brecha abismal entre algoritmos cuadráticos e ineficientes frente a los logarítmicos.
2. **`grafico_consumo_memoria.png`**: Muestra el incremento de memoria RAM asignado por el sistema operativo en cada caso.
3. **`grafico_comparativo_completo.png`**: Gráfico unificado en dos paneles (tiempo y memoria) para una vista integral.

---

## 5. Punto 4: Aplicación a un Conjunto de Datos Real

### 5.1. Datos del Archivo
* **Archivo:** `Demanda de celulares 2023.xlsx`
* **Registros totales:** 1,001 filas $\times$ 9 columnas.
* **Columna seleccionada:** `ganancia_neta` (tipo numérico entero: montos de ventas/ganancias).

### 5.2. Comparación entre Quick Sort y Merge Sort

| Algoritmo | Cantidad de Registros | Tiempo de Ejecución (s) | Consumo de RAM (MB) |
| :--- | :---: | :---: | :---: |
| **Quick Sort** | 1,001 | **0.002674 s** | 0.0039 MB |
| **Merge Sort** | 1,001 | **0.003349 s** | 0.0039 MB |

> **Diferencia:** Quick Sort resultó un **20.15% más rápido** que Merge Sort sobre el dataset real.

---

## 6. Conclusiones Finales (Punto 4.4)

### 1. ¿Cuál algoritmo fue el más rápido en promedio y por qué?
**Quick Sort** fue el más veloz en promedio (aproximadamente 0.032 s en datos aleatorios y 0.0026 s en el archivo real).  
*Justificación:* A pesar de que tanto Quick Sort como Merge Sort comparten una cota asintótica de $O(n \log n)$, Quick Sort tiene factores constantes de tiempo sustancialmente menores en hardware moderno. No requiere instanciar y concatenar listas temporales en cada paso como sí lo hace Merge Sort, y presenta una mayor localidad espacial de referencia, beneficiando el uso de la memoria caché del microprocesador.

### 2. ¿Cómo afectó el tipo de datos (ordenado, inverso, aleatorio) al rendimiento de cada algoritmo?
* **Bubble Sort e Insertion Sort:** Sufren drásticamente según la disposición de entrada. En listas ya ordenadas, su desempeño es sobresaliente ($\approx 0.001$ s, lineal $O(n)$). Sin embargo, frente a datos aleatorios o inversos caen a su comportamiento cuadrático $O(n^2)$, tardando entre 7 y 13 segundos para 10,000 elementos.
* **Merge Sort:** Demostró una estabilidad temporal absoluta. Tanto en datos aleatorios, ordenados o inversos, el tiempo rondó siempre entre 0.028 y 0.044 segundos, confirmando su naturaleza determinista de $O(n \log n)$.
* **Quick Sort:** Al implementar la partición con pivote en la mediana/centro, mantuvo un comportamiento $O(n \log n)$ parejo en las tres variantes (alrededor de 0.02 a 0.03 segundos), evitando la degradación a $O(n^2)$ que suele ocurrir cuando se toma arbitrariamente el primer o último valor como pivote.

### 3. ¿Qué algoritmo consideras el más eficiente para el uso general y por qué?
Para uso general en memoria principal, **Quick Sort** (o sus variantes híbridas como *Introsort* y *Timsort*) es el más eficiente debido a su sobresaliente velocidad práctica y menor consumo de memoria.  
No obstante, si la aplicación exige **estabilidad estricta** (mantener inalterado el orden relativo de registros con igual clave de ordenamiento) o si se deben ordenar datos almacenados en disco/secuenciales que no caben en memoria RAM, **Merge Sort** es la opción superior.

### 4. ¿Qué observaste en el análisis con el archivo real (`Demanda de celulares 2023.xlsx`)?
En un volumen de 1,001 registros, ambos algoritmos resolvieron el ordenamiento en menos de 3.5 milisegundos. A esta escala, la diferencia absoluta es prácticamente imperceptible para el usuario y el consumo adicional de memoria registrado a nivel de sistema operativo fue de apenas 0.0039 MB. Esto evidencia que los algoritmos de orden $O(n \log n)$ son extraordinariamente potentes y escalables para aplicaciones de negocio y análisis de datos en el mundo real.

---

## 7. Instrucciones de Ejecución

Para ejecutar la solución completa y visualizar los resultados:

```bash
# 1. Activar el entorno virtual o utilizar el python del proyecto
& "d:\Escritorio\Python POO\.venv\Scripts\python.exe" "d:\Escritorio\Python POO\TP-5\tp5_analisis_ordenamiento.py"

# O ejecutar los módulos individuales según necesidad:
& "d:\Escritorio\Python POO\.venv\Scripts\python.exe" "d:\Escritorio\Python POO\TP-5\punto_1_algoritmos.py"
& "d:\Escritorio\Python POO\.venv\Scripts\python.exe" "d:\Escritorio\Python POO\TP-5\punto_2_rendimiento.py"
& "d:\Escritorio\Python POO\.venv\Scripts\python.exe" "d:\Escritorio\Python POO\TP-5\punto_3_visualizacion.py"
& "d:\Escritorio\Python POO\.venv\Scripts\python.exe" "d:\Escritorio\Python POO\TP-5\punto_4_datos_reales.py"
```
