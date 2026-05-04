# Ejercicio 4 - Generador de reporte
# El programa muestra los números del 1 al 20
# y resalta cuáles son pares.

print("Reporte de números del 1 al 20")
print("------------------------------")

# range(1, 21) genera los números desde el 1 hasta el 20.
# El 21 no se incluye, por eso se usa como límite superior.

# Primer recorrido: mostramos todos los números.
for numero in range(1, 21):
    print(f"Número: {numero}")

print("------------------------------")
print("Números pares:")

# Segundo recorrido: mostramos solamente los números pares.
for numero in range(1, 21):

    # Si el resto de dividir el número por 2 es 0,
    # entonces el número es par.
    if numero % 2 == 0:
        print(numero)