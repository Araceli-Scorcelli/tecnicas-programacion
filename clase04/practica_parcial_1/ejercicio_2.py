notas = [7, 3, 9, 5, 6, 2, 8]

### Funcion filtrar aprobados
## •filtrar_aprobados(notas) → devuelve una lista con las notas mayores o iguales a 6.


def filtrar_aprobados(notas):

    lista_notas = []

    for nota in notas:

        if nota >= 6:

            lista_notas.append(nota)

    return lista_notas


### Funcion calcular el promedio total de las notas
## •calcular_promedio(notas) → devuelve el promedio de toda la lista.


def calcular_promedio(notas):

    acumulador = 0

    for nota in notas:

        acumulador = acumulador + nota

    return acumulador / len(notas)


### Funcion mostrar informa
## • mostrar_informe(aprobados, promedio) → muestra cuántos aprobaron, cuántos desaprobaron y el promedio general.


def mostrar_informe(aprobados, promedio):

    cantidad_aprobados = len(aprobados)
    cantidad_desaprobados = len(notas) - cantidad_aprobados

    print("Cantidad de aprobados:", cantidad_aprobados)
    print("Cantidad de desaprobados:", cantidad_desaprobados)
    print("Promedio general:", promedio)


##### Programa principal

aprobados = filtrar_aprobados(notas)
promedio = calcular_promedio(notas)

mostrar_informe(aprobados, promedio)
