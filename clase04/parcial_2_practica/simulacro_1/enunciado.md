  Ejercicio 1 — Clases y objetos   (50 pts)


Creá una clase Libro para representar los libros de una biblioteca. Cada libro tiene título, autor, año de publicación y cantidad de páginas.

La clase debe tener los siguientes métodos:
__init__(self, titulo, autor, anio, paginas)  →  inicializa los atributos del libro.

es_reciente()  →  retorna True si el libro fue publicado en los últimos 10 años (a partir de 2015), False en caso contrario.

actualizar_anio(nuevo_anio)  →  actualiza el año de publicación. Si el valor recibido es menor a 1800 o mayor a 2025, mostrar un mensaje de error y no modificar el atributo.

mostrar()  →  imprime los datos del libro. Ejemplo: "El Principito — Antoine de Saint-Exupéry (1943) | 96 páginas"

En el programa principal:
Creá al menos 2 instancias de Libro con datos distintos.
Llamá a mostrar() en cada uno.
Intentá actualizar el año con un valor inválido en uno de los libros. Verificá que la validación funcione.
Mostrá si cada libro es reciente o no.

⚠ Nota: No se evaluarán programas sin clases ni métodos.

  Ejercicio 2 — Herencia   (50 pts)


Extendé el sistema del Ejercicio 1 con dos subclases que hereden de Libro:

LibroDigital(Libro):
Atributo adicional: formato (por ejemplo: 'PDF', 'EPUB', 'MOBI').
Sobreescribí mostrar() para incluir el formato. Ejemplo: "Clean Code — Robert C. Martin (2008) | 431 páginas | Formato: PDF"
Método adicional convertir_formato(nuevo_formato)  →  cambia el formato del libro e imprime: "Formato actualizado a [nuevo_formato]."

LibroInfantil(Libro):

Atributo adicional: edad_recomendada (entero, edad mínima sugerida).

Sobreescribí mostrar() para incluir la edad. Ejemplo: "Donde viven los monstruos — Maurice Sendak (1963) | 48 páginas | Edad recomendada: 4 años"

Método adicional es_apto(edad_lector)  →  retorna True si la edad del lector es mayor o igual a la edad recomendada.

En el programa principal:
Creá al menos 1 instancia de cada subclase.
Guardá los tres libros (incluido el del Ejercicio 1) en una lista llamada biblioteca.
Recorré la lista e imprimí cada libro usando mostrar() (polimorfismo).
Si el libro es LibroInfantil, verificá si es apto para un lector de 6 años.

⚠ Nota: No se aceptan soluciones sin herencia ni super().
