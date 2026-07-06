ENUNCIADO

Ejercicio 1 - Clase base (50 puntos)

Creá una clase Vehiculo para representar los vehículos registrados en una flota. Cada vehículo tiene
marca, patente, año y un indicador booleano que informa si está habilitado.

 __init__(self, marca, patente, anio, habilitado): inicializa los atributos.

 puede_circular(): retorna True si el vehículo está habilitado y False en caso contrario.

 actualizar_anio(nuevo_anio): actualiza el año. Si es menor a 1990 o mayor a 2026, muestra un
error y no modifica el atributo.

 mostrar(): imprime los datos. Ejemplo: "Vehículo AA123BB - Toyota | Año: 2018 | Estado:
habilitado".

En el programa principal:
 Creá al menos dos instancias de Vehiculo con datos distintos.
 Llamá a mostrar() en cada una.
 Intentá actualizar el año con un valor inválido y verificá que no cambie.
 Mostrá si cada vehículo puede circular.

EJERCICIO 1
│
├── creo la clase base
├── creo dos objetos
└── pruebo sus métodos
         │
         ▼
EJERCICIO 2
│
├── conservo la clase base
├── agrego las subclases
├── conservo uno de los objetos anteriores
├── creo un objeto de cada subclase
├── los pongo juntos en una lista
└── recorro la lista

Ejercicio 2 - Herencia y polimorfismo (50 puntos)

Extendé el sistema con dos subclases que hereden de Vehiculo:

VehiculoElectrico(Vehiculo)
 Atributo adicional: autonomia, expresada en kilómetros.
 Sobreescribí mostrar() para incluir la autonomía.
 Método adicional actualizar_autonomia(nueva_autonomia): cambia la autonomía e imprime
"Autonomía actualizada a [valor] km".

VehiculoCarga(Vehiculo)
 Atributo adicional: carga_actual, expresada en kilogramos.
 Sobreescribí mostrar() para incluir la carga actual.
 Sobreescribí puede_circular(): solo retorna True si está habilitado y la carga actual es menor o igual a 1500 kg.

En el programa principal:
 Creá al menos una instancia de cada subclase.
 Guardá tres vehículos, incluido uno de la clase base, en una lista llamada flota.
 Recorré la lista y ejecutá mostrar() sobre cada objeto.
 Si el objeto es VehiculoCarga, indicá además si puede circular.

Condición obligatoria
La solución debe utilizar herencia y
super().__init__