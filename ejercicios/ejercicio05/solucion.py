cantidad_ventas = 0

total_vendido = 0

monto_ventas = float(input("Ingrese el monto de la venta o n° 0 para finalizar: "))

while monto_ventas != 0:

    cantidad_ventas = cantidad_ventas + 1

    total_vendido = total_vendido + monto_ventas

    monto_ventas = float(
        input("Ingrese otro monto de la venta o n° 0 para finalizar: ")
    )

print(f"Cantidad de ventas: {cantidad_ventas}")
print(f"Total vendido: {total_vendido}")
