# Punto 1: Implementacion de Algoritmos de Ordenamiento
# Alumno: Alfredo Patiño

# 1. Bubble Sort
def bubble_sort(arr):
    lista = list(arr)
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista

# 2. Insertion Sort
def insertion_sort(arr):
    lista = list(arr)
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# 3. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    mitad = len(arr) // 2
    izq = merge_sort(arr[:mitad])
    der = merge_sort(arr[mitad:])
    return mezclar(izq, der)

def mezclar(izq, der):
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
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# 4. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


if __name__ == "__main__":
    lista = [34, 12, 5, 23, 1, 99, 54]
    print("Lista original: ", lista)
    print("Bubble Sort:    ", bubble_sort(lista))
    print("Insertion Sort: ", insertion_sort(lista))
    print("Merge Sort:     ", merge_sort(lista))
    print("Quick Sort:     ", quick_sort(lista))
