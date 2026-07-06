"""Trabajá con el siguiente listado de temperaturas diarias (en °C):


temperaturas = [22, 35, 18, 40, 15, 31, 28, 12, 38, 20]
Escribí un programa con las siguientes funciones:
filtrar_calurosos(temperaturas)  → devuelve una lista solo con las temperaturas mayores a 30°C.
calcular_promedio(temperaturas)  → devuelve el promedio de todas las temperaturas.
mostrar_informe(calurosos, promedio)  → muestra cuántos días calurosos hubo, cuántos no, y el promedio.
⚠ Nota: No se aceptan soluciones sin funciones."""

temperaturas = [22, 35, 18, 40, 15, 31, 28, 12, 38, 20]

### Funcion Filtrar Temperatura
# filtrar_calurosos(temperaturas)  → devuelve una lista solo con las temperaturas mayores a 30°C.


def filtrar_calurosos(temperaturas):

    lista_temperatura = []

    for temperatura in temperaturas:

        if temperatura > 30:

            lista_temperatura.append(temperatura)

    return lista_temperatura


calurosos = filtrar_calurosos(temperaturas)

print("Temperaturas calurosas:", calurosos)

### Funcion Promedio de temperatura
# calcular_promedio(temperaturas)  → devuelve el promedio de todas las temperaturas.


def calcular_promedio(temperaturas):

    promedio = sum(temperaturas) / len(temperaturas)

    return promedio


promedio = calcular_promedio(temperaturas)

print(temperaturas)
print("El promedio de la temperatura es: ", promedio)
