# Ejercicio 2 - Control de acceso por edad

# El programa pide la edad del usuario 
# y determina qué tipo de acceso corresponde.

# < > <= >= == !=  

try:
    # input() pide la edad al usuario.
    # int() convierte el dato ingresado a número entero.
    edad = int(input("Ingrese su edad: "))

    # Caso borde: una edad negativa no es válida.
    if edad < 0:
        print("Error: la edad no puede ser negativa.") 
    
    # Si la edad es menor a 18, no puede ingresar.
    elif edad < 18: 
        print("Acceso denegado.")
    
    # Esta condición evalúa si la edad está dentro del rango 18 a 64 inclusive.
    elif 18 <= edad <= 64:
        print("Acceso permitido.")
    
    # Si no cumple las condiciones anteriores, entonces tiene 65 años o más.
    else:
        print("Acceso prioritario.")
    
# Si el usuario ingresa un dato que no puede convertirse a entero, se captura el error.
except ValueError:
    print ("Error: debe ingresar una edad númerica.")