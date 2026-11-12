# =====================================================================
# TRABAJO PRÁCTICO 5: ANÁLISIS DE ALGORITMOS DE ORDENAMIENTO
# PUNTO 1: Implementación de Algoritmos de Ordenamiento
# Materia: Algoritmos y Estructuras / POO
# Alumno: Alfredo Patiño
# =====================================================================

def bubble_sort(arr):
    """
    Algoritmo de Ordenamiento Burbuja (Bubble Sort).
    
    Compara pares de elementos adyacentes y los intercambia si están desordenados.
    Se incluye una bandera (swapped/intercambio) para optimizar el caso en que
    la lista ya se encuentre ordenada, permitiendo finalizar en O(n).
    
    Complejidad Temporal:
        - Mejor caso: O(n) (si ya está ordenada)
        - Caso promedio: O(n^2)
        - Peor caso: O(n^2) (orden inverso)
    Complejidad Espacial: O(1) auxiliar (sobre copia O(n)).
    """
    lista = list(arr)  # Trabajamos sobre una copia para no alterar la lista original
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        # Si en toda la pasada no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            break
    return lista


def insertion_sort(arr):
    """
    Algoritmo de Ordenamiento por Inserción (Insertion Sort).
    
    Construye la lista ordenada de manera incremental, tomando un elemento
    a la vez (clave) e insertándolo en su posición correspondiente dentro
    del segmento que ya fue ordenado.
    
    Complejidad Temporal:
        - Mejor caso: O(n) (si ya está ordenada)
        - Caso promedio: O(n^2)
        - Peor caso: O(n^2) (orden inverso)
    Complejidad Espacial: O(1) auxiliar.
    """
    lista = list(arr)
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Desplazamos los elementos mayores que la clave hacia la derecha
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def merge_sort(arr):
    """
    Algoritmo de Ordenamiento por Mezcla (Merge Sort).
    
    Aplica la técnica de diseño 'Divide y Vencerás' (Divide and Conquer).
    Divide recursivamente la lista a la mitad hasta llegar a sublistas de 1 elemento
    y luego las combina (mezcla) en orden ascendente.
    
    Complejidad Temporal:
        - Mejor caso: O(n log n)
        - Caso promedio: O(n log n)
        - Peor caso: O(n log n)
    Complejidad Espacial: O(n) de memoria auxiliar por las sublistas.
    """
    if len(arr) <= 1:
        return list(arr)

    mitad = len(arr) // 2
    izquierda = merge_sort(arr[:mitad])
    derecha = merge_sort(arr[mitad:])

    return _mezclar(izquierda, derecha)


def _mezclar(izquierda, derecha):
    """Función auxiliar de merge_sort para intercalar dos sublistas ordenadas."""
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregamos los elementos restantes (si quedan)
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def quick_sort(arr):
    """
    Algoritmo de Ordenamiento Rápido (Quick Sort).
    
    Aplica 'Divide y Vencerás'. Selecciona un elemento pivote y particiona la lista
    en elementos menores, iguales y mayores.
    Se utiliza el elemento central como pivote (arr[len(arr) // 2]) para evitar
    el peor caso O(n^2) y desbordes de recursión (RecursionError) cuando la lista
    ya está ordenada o en orden inverso.
    
    Complejidad Temporal:
        - Mejor caso: O(n log n)
        - Caso promedio: O(n log n)
        - Peor caso: O(n^2) (ocurre si el pivote elegido es consistentemente el extremo)
    Complejidad Espacial: O(n) en esta implementación recursiva funcional.
    """
    if len(arr) <= 1:
        return list(arr)

    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


# =====================================================================
# PRUEBAS UNITARIAS DE VERIFICACIÓN
# =====================================================================
if __name__ == "__main__":
    print("--- Verificando el funcionamiento de los algoritmos del Punto 1 ---")
    lista_prueba = [64, 34, 25, 12, 22, 11, 90, -5, 0, 22]
    esperado = sorted(lista_prueba)

    print("Lista original:  ", lista_prueba)
    print("Bubble Sort:     ", bubble_sort(lista_prueba))
    print("Insertion Sort:  ", insertion_sort(lista_prueba))
    print("Merge Sort:      ", merge_sort(lista_prueba))
    print("Quick Sort:      ", quick_sort(lista_prueba))

    assert bubble_sort(lista_prueba) == esperado, "Error en Bubble Sort"
    assert insertion_sort(lista_prueba) == esperado, "Error en Insertion Sort"
    assert merge_sort(lista_prueba) == esperado, "Error en Merge Sort"
    assert quick_sort(lista_prueba) == esperado, "Error en Quick Sort"
    print("\n¡Todos los algoritmos ordenaron los datos correctamente!")
