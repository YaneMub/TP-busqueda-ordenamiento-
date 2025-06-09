# ESTILOS PARA DESTACAR LOS TÍTULOS DE LOS ALGORITMOS EN CONSOLA:

from colorama import Fore, Style, init
init(autoreset=True)  


# LISTA BASE:

productos = [4021, 1500, 3200, 873, 2999, 1002, 789, 4300, 2200, 1450, 5000, 3900, 2800, 600, 350, 7500, 3100]
buscar_codigo = 2999


#ALGORITMOS DE BÚSQUEDA

"""BÚSQUEDA LINEAL"""

def busqueda_lineal(lista,codigo):
    for i in range(len(lista)):
        if lista[i] == codigo:
            return i
    return -1 #indica que no se encontró el elemento buscado. 

print(Style.BRIGHT + Fore.CYAN + "\nBÚSQUEDA LINEAL")
print(f"El código {buscar_codigo} se encuentra en la posición:", busqueda_lineal(productos, buscar_codigo))



"""BÚSQUEDA BINARIA"""

lista_ordenada = sorted(productos)

def busqueda_binaria(lista,codigo):
    izquierda, derecha = 0, len(lista) -1 #Utilizamos una asignación múltiple (en lugar de izquierda = 0 y derecha = len(lista) -1)
    while izquierda <= derecha: 
        medio = (izquierda + derecha) // 2
        if lista[medio] == codigo:
            return medio
        elif lista[medio] < codigo:
            izquierda = medio + 1
        else:
            derecha = medio -1 
    return -1 #indica que no se encontró el elemento buscado. 

print(Style.BRIGHT + Fore.CYAN + "\nBÚSQUEDA BINARIA")
print(f"El código {buscar_codigo} se encuentra en la posición:", busqueda_binaria(lista_ordenada, buscar_codigo))


# ALGORITMOS DE ORDENAMIENTO

"""Bubble Sort
Compara elementos adyacentes e intercambia si están en orden incorrecto. | Repite pasadas hasta que no hay más cambios.
"""

def bubble_sort(lista):
    datos = lista.copy()  # Copiamos la lista y la almacenamos en "datos" para no modificar la lista original. 
    n = len(datos)

    for i in range(n): # Iteramos el bucle n cantidad veces.
        for j in range(0, n-i-1): 
            # Tomamos el valor del elemento en posición j, e indicamos que el bucle recorra desde 0 hasta n (ctdad de valores) 
            # - i (n° de iteración del bucle "padre") -1. 
            # De esta forma se indica cuántos pares de combinaciones hacer en cada iteración de for i
            if datos[j] > datos[j+1]: 
                # Si el valor de j es mayor que el de j + 1 (la posición que le sigue)
                # Intercambiamos los valores.
                datos[j], datos[j+1] = datos[j+1], datos[j] 
    return datos

print(Style.BRIGHT + Fore.GREEN + "\nORDENAMIENTO: Bubble Sort")
print(f"Resultado:", bubble_sort(productos))


"""Selection Sort
Encuentra el menor elemento y lo pone al principio. | Repite para el resto de la lista.
"""

def selection_sort(lista):
    datos = lista.copy() # Copiamos la lista para no modificar la original.
    n = len(datos)

    for i in range(n): # Recorremos desde el primer hasta el último elemento de la lista datos. 
        menor = i # Suponemos que el mínimo está en i.

        for j in range(i + 1, n): # Recoremos desde i + 1 (para no comparar un valor consigo mismo) hasta n. 
            if datos[j] < datos[menor]: # Comparamos, si el valor de la posición datos[j] es menor que "menor", y actualizamos el valor de "menor".
                menor = j
        datos[i], datos[menor] = datos[menor], datos[i] # Ordenamos los valores de menor a mayor. 
    return datos 
    
    #  Repetimos el proceso (for i... for j...) hasta que todos los elementos de la lsita esten ordenados.

print(Style.BRIGHT + Fore.GREEN + "\nORDENAMIENTO: Selection Sort")
print(f"Resultado:", selection_sort(productos))


"""Insertion Sort
Toma un elemento y lo inserta en su lugar correcto en la parte ya ordenada de la lista.
"""

def insertion_sort(lista):
    datos = lista.copy() # Duplicamos la lista para no afectar a la original.

    for i in range(1, len(datos)): # Recorremos todos los elementos de la lista comenzando en 1.
        valor = datos[i] 
        j = i - 1 # Comparamos hacia atrás, desde el valor anterior. 

        while j >= 0 and datos[j] > valor: # Si j es mayor que valor
            datos[j + 1] = datos[j] # Reemplazamos j + 1 (que sería la posición de i) por el valor de j (de esta forma desplazamos el valor mayor a la derecha)
            j -= 1 # Seguimos hacia la izquierda.
        datos[j + 1] = valor # Colocamos el valor menor en "valor".
    return datos

print(Style.BRIGHT + Fore.GREEN + "\nORDENAMIENTO: Insertion Sort")
print(f"Resultado:", insertion_sort(productos))


"""Quick Sort
Divide la lista en menores y mayores que un pivote. | Ordena recursivamente.
"""

def quick_sort(lista):
    # Caso base: si tiene 1 o 0 elementos, ya está ordenada.
    if len(lista) <= 1:
        return lista
    else:
        # Elegimos el primer elemento como pivote
        pivote = lista[0]

        # Creamos dos listas:
        # 'menores' va a contener los elementos menores o iguales al pivote
        # 'mayores' va a contener los elementos mayores al pivote
        menores = [x for x in lista[1:] if x <= pivote] # x for x in... es una forma abreviada de escribir un bucle. 
        mayores = [x for x in lista[1:] if x > pivote]  # lista[1:] es una sublista, desde el segundo elemento en adelante.

        # Llamamos recursivamente a quick_sort sobre cada sublista
        # y luego unimos: primero los menores ordenados, luego el pivote, luego los mayores ordenados
        return quick_sort(menores) + [pivote] + quick_sort(mayores)
    
print(Style.BRIGHT + Fore.GREEN + "\nORDENAMIENTO: Quick Sort")
print(f"Resultado:", quick_sort(productos))