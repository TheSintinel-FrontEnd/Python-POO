

**Trabajo Práctico: Análisis de Algoritmos de Ordenamiento**

**Objetivos**

* Comprender el funcionamiento y las diferencias entre algoritmos de ordenamiento eficientes e ineficientes.  
* Medir y comparar el tiempo de ejecución y el consumo de memoria de cada algoritmo.  
* Analizar cómo el tipo de datos (ordenados, inversos, aleatorios) afecta al rendimiento de los algoritmos.  
* Aplicar los algoritmos a un conjunto de datos real (archivo CSV o Excel) para un análisis práctico.  
* Visualizar los resultados a través de gráficos para una comparación clara.

---

**Punto 1: Implementación de Algoritmos de Ordenamiento**

Implementa las siguientes funciones de ordenamiento. Si ya tienes el código de ejercicios anteriores, puedes reutilizarlo.

* bubble\_sort(arr): Implementa el algoritmo de ordenamiento de burbuja.  
* quick\_sort(arr): Implementa el algoritmo de ordenamiento rápido.  
* merge\_sort(arr): Implementa el algoritmo de ordenamiento por mezcla.  
* insertion\_sort(arr): Implementa el algoritmo de ordenamiento por inserción.

---

**Punto 2: Análisis del Rendimiento con Diferentes Tipos de Datos**

Crea un script principal que realice las siguientes acciones:

1. **Generación de Datos**: Escribe una función que cree tres listas de datos del mismo tamaño (por ejemplo, 10,000 elementos):  
   * Una lista de números **aleatorios**.  
   * Una lista de números **ordenados en orden inverso**.  
2. **Función de Medición**: Crea una función llamada medir\_rendimiento(algoritmo, datos). Esta función debe:  
   * Medir el **tiempo de ejecución** del algoritmo.  
   * Medir el **consumo de memoria RAM** usando la librería psutil (recuerda que debes instalarla con pip install psutil).  
3. **Ejecución y Recopilación**: Itera sobre cada tipo de dato (aleatorio, ordenado, inverso) y sobre cada algoritmo de ordenamiento. Llama a la función medir\_rendimiento para cada combinación y almacena los resultados (tiempo y memoria) en una estructura de datos (por ejemplo, diccionarios o listas).

---

**Punto 3: Visualización de Resultados**

Utiliza la librería matplotlib para generar gráficos que muestren los resultados de la comparación del Punto 2\.

1. **Gráfica de Tiempo**: Crea un gráfico de barras que compare el tiempo de ejecución de todos los algoritmos para cada tipo de dato. Puedes usar subgráficos o diferentes colores para distinguir los tipos de datos. El eje Y debe ser el tiempo en segundos.  
2. **Gráfica de Memoria**: Crea otro gráfico de barras para comparar el consumo de memoria RAM de los mismos algoritmos en cada tipo de dato. El eje Y debe ser el consumo en MB.

---

**Punto 4: Aplicación a un Conjunto de Datos Real**

Ahora, aplica lo aprendido a un archivo de datos real.

1. **Carga de Archivo**: Utiliza pandas para cargar un archivo de datos de tipo **CSV** o **Excel**. Si no tienes uno, puedes crear uno con datos de ejemplo. La función a usar es pd.read\_csv() o pd.read\_excel().  
   * **Nota**: Si usas Excel, necesitarás instalar openpyxl con pip install openpyxl.  
2. **Selección de Columna**: Elige una columna numérica del archivo que quieras ordenar. Es crucial que los datos de esa columna sean numéricos para que los algoritmos funcionen.  
3. **Análisis Final**: Mide y compara el tiempo y la memoria de quick\_sort y merge\_sort con los datos de tu archivo. ¿Cuál es más rápido? ¿Hay alguna diferencia significativa en el consumo de memoria?  
4. **Conclusión**: Redacta un pequeño informe (puedes usar un bloque de comentarios en el mismo script) que resuma tus hallazgos. Incluye:  
   * ¿Cuál algoritmo fue el más rápido en promedio y por qué?  
   * ¿Cómo afectó el tipo de datos (ordenado, inverso, aleatorio) al rendimiento de cada algoritmo?  
   * ¿Qué algoritmo consideras el más eficiente para el uso general y por qué?  
   * ¿Qué observaste en el análisis con el archivo real?

Método de calificación

| PUNTO A EVALUAR |  PUNTAJE TEORICO | PUNTAJE OBTENIDO |
| :---- | ----- | :---- |
| PUNTO 1 | 2 puntos |  |
| PUNTO 2 | 2 puntos |  |
| PUNTO 3 | 2 puntos |  |
| PUNTO 4 | 4 puntos |  |
| Total | 10 puntos |  |

