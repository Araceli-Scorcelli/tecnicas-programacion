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
            f"Socio #{self.numero} — {self.nombre} | "
            f"{self.edad} años | Cuota: {cuota_estado}"
        )


class SocioVIP(Socio):

    def __init__(self, nombre, numero, edad, cuota_al_dia, beneficios):
        super().__init__(nombre, numero, edad, cuota_al_dia)
        self.beneficios = beneficios

    def mostrar(self):
        if self.cuota_al_dia:
            cuota_estado = "al día"
        else:
            cuota_estado = "no al día"

        beneficios_str = ", ".join(self.beneficios)

        print(
            f"Socio #{self.numero} — {self.nombre} | "
            f"{self.edad} años | Cuota: {cuota_estado} | "
            f"Beneficios: {beneficios_str}"
        )

    def agregar_beneficio(self, beneficio):
        self.beneficios.append(beneficio)
        print(f"Beneficio agregado: {beneficio}.")


class SocioMenor(Socio):

    def __init__(self, nombre, numero, edad, cuota_al_dia, tutor):
        super().__init__(nombre, numero, edad, cuota_al_dia)
        self.tutor = tutor

    def mostrar(self):
        if self.cuota_al_dia:
            cuota_estado = "al día"
        else:
            cuota_estado = "no al día"

        print(
            f"Socio #{self.numero} — {self.nombre} | "
            f"{self.edad} años | Cuota: {cuota_estado} | "
            f"Tutor: {self.tutor}"
        )

    def puede_ingresar(self):
        return self.cuota_al_dia and self.edad >= 12


# Programa principal

socio_comun = Socio("María López", 1042, 34, True)

socio_vip = SocioVIP("Carlos Ruiz", 2045, 41, True, ["Sauna", "Clases grupales"])

socio_menor = SocioMenor("Valentina Torres", 89, 15, True, "Ana Torres")

gimnasio = [socio_comun, socio_vip, socio_menor]

for socio in gimnasio:
    socio.mostrar()

    if isinstance(socio, SocioMenor):
        if socio.puede_ingresar():
            print("Puede ingresar al gimnasio.")
        else:
            print("No puede ingresar al gimnasio.")

    print("-" * 40)
