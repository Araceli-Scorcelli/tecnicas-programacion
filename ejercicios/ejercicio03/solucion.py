# Ejercicio 3 - Comparación de productos
# El programa recibe el precio de dos productos, compara cuál es más caro
# y muestra la diferencia de precio entre ambos.

try:  
    # Pedimos el precio del primer producto.
    # float() permite ingresar números con decimales.

    precio_producto_1 = float (input ("Ingrese el precio del primer producto: "))

    precio_producto_2 = float (input ("Ingrese el precio del segundo producto: "))

    # Calculamos la diferencia de precio usando abs()
    # para que el resultado siempre sea positivo.
    diferencia = abs(precio_producto_1 - precio_producto_2)

    if precio_producto_1 > precio_producto_2: 
       print("El primer producto es mas caro.")
    
    # Si el segundo producto cuesta más que el primero, es el más caro.
    elif precio_producto_2 > precio_producto_1: 
        print("El segundo producto es mas caro.")
    
    # Si no se cumple ninguna de las condiciones anteriores,
    # significa que ambos precios son iguales.

    else:
        print("Ambos productos tienen el mismo precio")

    # Mostramos la diferencia de precio.
    print(f"La diferencia de precio es: {diferencia}")

# Si el usuario ingresa un dato no numérico, se captura el error.
except ValueError:
    print("Error: debe ingresar precios numéricos.")