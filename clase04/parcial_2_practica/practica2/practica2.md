Extendé el sistema del Ejercicio 1 con dos subclases que hereden de Socio:

SocioVIP(Socio):
•	Atributo adicional: beneficios (una lista de strings, por ejemplo: ['Clases grupales', 'Sauna', 'Estacionamiento']).
•	Sobreescribí mostrar() para incluir los beneficios. Ejemplo: "Socio #0021 — Carlos Ruiz | 41 años | Cuota: al día | Beneficios: Clases grupales, Sauna"
•	Método adicional agregar_beneficio(beneficio)  →  agrega un string a la lista de beneficios e imprime: "Beneficio agregado: [beneficio]."

SocioMenor(Socio):
•	Atributo adicional: tutor (nombre del tutor o responsable).
•	Sobreescribí mostrar() para incluir el tutor. Ejemplo: "Socio #0089 — Valentina Torres | 15 años | Cuota: al día | Tutor: Ana Torres"
•	Sobreescribí puede_ingresar() para que solo pueda ingresar si la cuota está al día y la edad es mayor o igual a 12.

En el programa principal:
•	Creá al menos 1 instancia de cada subclase.
•	Guardá los tres socios (incluido el del Ejercicio 1) en una lista llamada gimnasio.
•	Recorré la lista e imprimí cada socio usando mostrar() (polimorfismo).
•	Si el socio es SocioMenor, indicá además si puede ingresar.

"""

class Socio:
    def __init__(self, nombre, numero, edad, cuota_al_dia):
        self.nombre = nombre
        self.numero = numero
        self.edad = edad
        self.cuota_al_dia = cuota_al_dia

    def puede_ingresar(self):
        return self.cuota_al_dia

    def actualizar_edad(self, nueva_edad):
        if nueva_edad < 0 or nueva_edad > 120:
            print("Error: La edad debe estar entre 0 y 120 años.")
        else:
            self.edad = nueva_edad

    def mostrar(self):
        if self.cuota_al_dia:
            cuota_estado = "al día"
        else:
            cuota_estado = "no al día"

        print(f"Socio #{self.numero} — {self.nombre} | {self.edad} años | Cuota: {cuota_estado}")

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
        print(f"Socio #{self.numero} — {self.nombre} | {self.edad} años | Cuota: {cuota_estado} | Beneficios: {beneficios_str}")

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

        print(f"Socio #{self.numero} — {self.nombre} | {self.edad} años | Cuota: {cuota_estado} | Tutor: {self.tutor}")

    def puede_ingresar(self):
        return self.cuota_al_dia and self.edad >= 12
    
# Programa principal
socio1 = Socio("María López", 1042, 34, True)
socio_vip = SocioVIP("Carlos Ruiz", 21, 41, True, ["Clases grupales", "Sauna"])
socio_menor = SocioMenor("Valentina Torres", 89, 15, True, "Ana Torres")

gimnasio = [socio1, socio_vip, socio_menor]

for socio in gimnasio:
    socio.mostrar()
    if isinstance(socio, SocioMenor):
        if socio.puede_ingresar():
            print(f"puede ingresar al gimnasio.")
        else:
            print(f"no puede ingresar al gimnasio.")