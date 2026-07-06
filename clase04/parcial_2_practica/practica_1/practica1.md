"""Creá una clase Socio para representar los miembros de un gimnasio. Cada socio tiene nombre, número de socio, edad y si tiene la cuota al día (booleano).

La clase debe tener los siguientes métodos:

•	__init__(self, nombre, numero, edad, cuota_al_dia)  →  inicializa los atributos del socio.

•	puede_ingresar()  →  retorna True si la cuota está al día, False en caso contrario.

•	actualizar_edad(nueva_edad)  →  actualiza la edad del socio. Si el valor recibido es menor a 0 o mayor a 120, mostrar un mensaje de error y no modificar el atributo.

•	mostrar()  →  imprime los datos del socio. Ejemplo: "Socio #1042 — María López | 34 años | Cuota: al día"

En el programa principal:
•	Creá al menos 2 instancias de Socio con datos distintos.
•	Llamá a mostrar() en cada uno.
•	Intentá actualizar la edad con un valor inválido. Verificá que la validación funcione.
•	Mostrá si cada socio puede ingresar o no.
"""


