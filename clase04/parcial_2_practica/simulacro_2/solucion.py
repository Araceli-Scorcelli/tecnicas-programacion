# =========================
# CLASE BASE
# =========================


class Vehiculo:

    def __init__(self, marca, patente, anio, habilitado):
        self.marca = marca
        self.patente = patente
        self.anio = anio
        self.habilitado = habilitado

    def puede_circular(self):
        return self.habilitado

    def actualizar_anio(self, nuevo_anio):
        if 1990 <= nuevo_anio <= 2026:
            self.anio = nuevo_anio
        else:
            print(
                "Fecha inválida: el año de fabricación " "debe estar entre 1990 y 2026."
            )

    def mostrar(self):
        if self.habilitado:
            estado = "habilitado"
        else:
            estado = "no habilitado"

        print(
            f"Vehículo {self.patente} - {self.marca} | "
            f"Año: {self.anio} | Estado: {estado}"
        )


# =========================
# PRIMERA SUBCLASE
# =========================


class VehiculoElectrico(Vehiculo):

    def __init__(self, marca, patente, anio, habilitado, autonomia):
        super().__init__(marca, patente, anio, habilitado)

        self.autonomia = autonomia

    def mostrar(self):
        if self.habilitado:
            estado = "habilitado"
        else:
            estado = "no habilitado"

        print(
            f"Vehículo {self.patente} - {self.marca} | "
            f"Año: {self.anio} | Estado: {estado} | "
            f"Autonomía: {self.autonomia} km"
        )

    def actualizar_autonomia(self, nueva_autonomia):
        self.autonomia = nueva_autonomia

        print(f"Autonomía actualizada a " f"{nueva_autonomia} km.")


# =========================
# SEGUNDA SUBCLASE
# =========================


class VehiculoCarga(Vehiculo):

    def __init__(self, marca, patente, anio, habilitado, carga_actual):
        super().__init__(marca, patente, anio, habilitado)

        self.carga_actual = carga_actual

    def mostrar(self):
        if self.habilitado:
            estado = "habilitado"
        else:
            estado = "no habilitado"

        print(
            f"Vehículo {self.patente} - {self.marca} | "
            f"Año: {self.anio} | Estado: {estado} | "
            f"Carga actual: {self.carga_actual} kg"
        )

    def puede_circular(self):
        return self.habilitado and self.carga_actual <= 1500


# =========================
# PROGRAMA PRINCIPAL
# =========================

# Objetos de la clase base

vehiculo_comun_1 = Vehiculo("Toyota", "AA123BB", 2018, True)

vehiculo_comun_2 = Vehiculo("Renault", "BB321AA", 2017, False)


# Pruebas del Ejercicio 1

print("PRUEBAS DEL EJERCICIO 1")
print("-" * 40)

vehiculo_comun_1.mostrar()
vehiculo_comun_2.mostrar()

print(f"¿Puede circular?: " f"{vehiculo_comun_1.puede_circular()}")

print(f"¿Puede circular?: " f"{vehiculo_comun_2.puede_circular()}")

# Prueba con un año inválido

vehiculo_comun_1.actualizar_anio(1800)

# Verificamos que el año no cambió

vehiculo_comun_1.mostrar()


# Objetos del Ejercicio 2

vehiculo_electrico = VehiculoElectrico("Renault", "CC456DD", 2024, True, 320)

vehiculo_carga = VehiculoCarga("Iveco", "EE789FF", 2016, True, 1700)


# Prueba del método actualizar_autonomia

vehiculo_electrico.mostrar()

vehiculo_electrico.actualizar_autonomia(400)

vehiculo_electrico.mostrar()

# Lista con los tres objetos

flota = [vehiculo_comun_1, vehiculo_electrico, vehiculo_carga]


# Recorrido y polimorfismo

print()
print("PRUEBAS DEL EJERCICIO 2")
print("-" * 40)

for vehiculo in flota:
    vehiculo.mostrar()

    if isinstance(vehiculo, VehiculoCarga):
        if vehiculo.puede_circular():
            print("Puede circular con la carga actual.")
        else:
            print("No puede circular con la carga actual.")

    print("-" * 40)
