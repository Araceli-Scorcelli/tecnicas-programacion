# Ejercicio 1 - Clasificación de temperatura
# El programa pide una temperatura al usuario y la clasifica según su valor.

try:
    # input() pide un dato al usuario.
    # int() convierte ese dato a número entero.
    temperatura = int(input("Ingrese una temperatura: "))

    # Si la temperatura es menor que 0, se considera bajo cero.
    if temperatura < 0:
        print("La temperatura está bajo cero.")

    # Esta condición evalúa si la temperatura está dentro del rango 0 a 25 inclusive.
    # Es decir: temperatura debe ser mayor o igual a 0 y menor o igual a 25.    
    elif 0 <= temperatura <= 25:
        print("La temperatura es templada.")
  
   # Si no cumple las condiciones anteriores, entonces necesariamente es mayor a 25.
    else:
        print("La temperatura es alta.")

# Si el usuario ingresa algo que no puede convertirse a entero, se captura el error.
except ValueError:
    print("Error: debe ingresar un número entero.")