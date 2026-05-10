# Ejercicio 8 - Análisis de datos
# Dada una lista de números, el programa calcula:
# suma total, promedio y valor máximo sin usar sum() ni max().

numeros = [10, 25, 7, 40, 15]

# Acumulador para guardar la suma total de los números.
total = 0

# Contador para saber cuántos números hay en la lista.
cantidad = 0

# Tomamos el primer número como máximo inicial.
maximo = numeros[0]

# Recorremos cada número de la lista.
for numero in numeros:

    # Sumamos el número actual al total.
    total = total + numero

    # Contamos cuántos números vamos recorriendo.
    cantidad = cantidad + 1

    # Si el número actual es mayor que el máximo guardado,
    # actualizamos la variable maximo.
    if numero > maximo:
        maximo = numero

# Calculamos el promedio dividiendo el total por la cantidad de números.
promedio = total / cantidad

print("La suma total es:", total)
print("El promedio es:", promedio)
print("El valor máximo es:", maximo)
