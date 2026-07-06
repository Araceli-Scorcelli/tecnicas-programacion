class Socio:

    def __init__(self, nombre, numero, edad, cuota_al_dia):
        self.nombre = nombre
        self.numero = numero
        self.edad = edad
        self.cuota_al_dia = cuota_al_dia

    def puede_ingresar(self):
        return self.cuota_al_dia

    def actualizar_edad(self, nueva_edad):
        if 0 <= nueva_edad <= 120:
            self.edad = nueva_edad
        else:
            print("Error: la edad debe estar entre 0 y 120.")

    def mostrar(self):
        if self.cuota_al_dia:
            cuota_estado = "al día"
        else:
            cuota_estado = "no al día"

        print(
            f"Socio #{self.numero} — {self.nombre} | {self.edad} años | Cuota: {cuota_estado}"
        )


# Programa principal
socio1 = Socio("María López", 1042, 34, True)
# socio2 = Socio("Juan Pérez", 2045, 28, False)

socio1.mostrar()
# socio2.mostrar()

# Intentar actualizar la edad con un valor inválido
socio1.actualizar_edad(200)  # Edad inválida
socio1.mostrar()  # Mostrar los datos actualizados del socio
