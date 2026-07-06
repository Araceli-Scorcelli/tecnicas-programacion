# Escribí un programa modular con las siguientes funciones:
# • pedir_notas() → pide 5 notas al usuario y las devuelve en una lista.
# • calcular_promedio(notas) → recibe la lista y devuelve el promedio.
# • guardar_resultado(promedio) → guarda en resultado.txt el promedio y si el
# alumno aprueba (>= 6) o no. Si el archivo no se puede crear, debe mostrar un
# mensaje de error en lugar de romperse.
# El programa principal debe llamar a las tres funciones en orden.
# ⚠ Nota: No se aceptan soluciones sin funciones ni sin manejo de error en el archivo

## Funcion pedir notas al usuario
## pedir_notas() → pide 5 notas al usuario y las devuelve en una lista.


def pedir_notas():

    notas = []

    for i in range(5):

        nota = float(input("Ingresar Notas: "))
        notas.append(nota)

    return notas


## Funcion promedio
## • calcular_promedio(notas) → recibe la lista y devuelve el promedio.


def calcular_promedio(notas):

    promedio = sum(notas) / len(notas)

    return promedio


## Funcion promedio
## • calcular_promedio(notas) → recibe la lista y devuelve el promedio.


def guardar_resultado(promedio):

    try:
        archivo_promedio = open("resultado.txt", "w")

        archivo_promedio.write("Promedio: " + str(promedio) + "\n")

        if promedio >= 6:
            archivo_promedio.write("El alumno aprueba")
        else:
            archivo_promedio.write("El alumno no aprueba")

        archivo_promedio.close()

        print("Resultado guardado correctamente")

    except:
        print("No se puede abrir o crear el archivo")


notas = pedir_notas()
promedio = calcular_promedio(notas)
guardar_resultado(promedio)
