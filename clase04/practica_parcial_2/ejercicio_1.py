##Escribí un programa que pida al usuario palabras hasta que ingrese la palabra 'fin'. Al finalizar, mostrá cuántas palabras ingresó y cuál tiene más letras.
## El programa debe organizarse con las siguientes funciones:
## pedir_palabras()  → pide palabras al usuario hasta que ingrese 'fin' y las devuelve en una lista.
## analizar(palabras)  → recibe la lista y devuelve la cantidad y la palabra más larga.
## mostrar_resultados(cantidad, mas_larga)  → muestra los resultados por pantalla.
## ⚠ Nota: No se aceptan soluciones sin funciones.


## Funcion pedir_palabras()  → pide palabras al usuario hasta que ingrese 'fin' y las devuelve en una lista.


def pedir_palabras():

    lista_palabras = []

    palabra = input("Escriba la palabra que desea ingresar: ")

    while palabra != "fin":

        lista_palabras.append(palabra)

        palabra = input(
            "Escriba otra palabra que desee ingresar o ingrese fin para finalizar: "
        )

    return lista_palabras


def analizar(palabras):

    cantidad = len(palabras)

    if cantidad == 0:
        mas_larga = None

    else:
        mas_larga = palabras[0]

        for palabra in palabras:

            if len(palabra) > len(mas_larga):

                mas_larga = palabra

    return cantidad, mas_larga


palabras = pedir_palabras()

print("Palabras ingresadas:")
print(*palabras, sep="\n")

cantidad, mas_larga = analizar(palabras)

print("Cantidad de palabras:", cantidad)
print("Palabra más larga:", mas_larga)
