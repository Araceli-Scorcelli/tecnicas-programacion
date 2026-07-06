productos = ["pan", "arroz", "leche", "queso", "azucar", "almendras"]

producto_buscado = input("Ingrese el producto que desea buscar: ")

contador = 0
encontrado = False
posicion = -1

# len(productos) devuelve cuántos elementos tiene la lista.
# #Lo que significa que: Mientras el contador sea menor que la cantidad de productos,
# seguí buscando.Cuando el contador llega a 5, corta, porque ya no hay más productos.

while True:
    menu = int(input("1 seguir 0- salir"))
    if menu == 1:

        while contador < len(productos):

            # En esta linea se pide, el producto que está en la posición actual del contador.

            producto_actual = productos[contador]

            # se chequea que el producto que estoy mirando es igual al que pidió el usuario.
            # Si es asi, guardás que lo encontraste y en qué posición estaba.
            if producto_actual == producto_buscado:
                encontrado = True
                posicion = contador

            contador = contador + 1

            if encontrado:
                print(f"El producto existe en la lista.")
                print(f"Está en la posición: {posicion}")
            else:
                print("El producto no existe en la lista.")

    elif menu == 0:
        break
