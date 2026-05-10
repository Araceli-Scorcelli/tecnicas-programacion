contador = 0
contraseña = ""

while contraseña != "admin123":

    contraseña = input("Ingresar contraseña: ")

    contador = contador + 1

    if contraseña != "admin123":
        print("Contraseña incorrecta, intente nuevamente.")
        print(f"Cantidad de intentos: {contador}")

print("Acceso concedido")
