# < > <= >= == !=

##### Funcion pedir numeros al usuario


def pedir_numeros():

    lista = []
    numero = int(
        input("Ingrese un numero entero para comenzar o negativo para finalizar: ")
    )

    while numero >= 0:

        lista.append(numero)
        numero = int(input("Ingrese otro numero entero para continuar: "))

    if numero < 0:

        print("Finalizo el ingreso, selecciono un numero negativo ")

    return lista


##### Funcion analizar lista.


def analizar(numeros):

    cantidad = len(numeros)

    if cantidad == 0:

        mayor = None

    else:
        mayor = max(numeros)

    return cantidad, mayor


##### Funcion mostrar lista


def mostrar_resultados(cantidad, mayor):

    print("Cantidad de numeros ingresados:", cantidad)

    if mayor == None:
        print("No se ingresaron numeros positivos o cero.")
    else:
        print("El numero mayor es:", mayor)


##### Programa principal

numeros = pedir_numeros()

cantidad, mayor = analizar(numeros)

mostrar_resultados(cantidad, mayor)
