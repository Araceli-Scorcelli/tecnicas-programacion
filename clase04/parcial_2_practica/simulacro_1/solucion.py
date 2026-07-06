class Libro:

    def __init__(self, titulo, autor, anio, paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.paginas = paginas

    def es_reciente(self):
        return 2015 <= self.anio <= 2025

    def actualizar_anio(self, nuevo_anio):
        if 1800 <= nuevo_anio <= 2025:
            self.anio = nuevo_anio
        else:
            print(
                "Fecha inválida: el año de publicación " "debe estar entre 1800 y 2025."
            )

    def mostrar(self):
        print(
            f"{self.titulo} — {self.autor} " f"({self.anio}) | {self.paginas} páginas"
        )


class LibroDigital(Libro):

    def __init__(self, titulo, autor, anio, paginas, formato):
        super().__init__(titulo, autor, anio, paginas)
        self.formato = formato

    def mostrar(self):
        print(
            f"{self.titulo} — {self.autor} "
            f"({self.anio}) | {self.paginas} páginas | "
            f"Formato: {self.formato}"
        )

    def convertir_formato(self, nuevo_formato):
        self.formato = nuevo_formato
        print(f"Formato actualizado a {nuevo_formato}.")


class LibroInfantil(Libro):
    def __init__(self, titulo, autor, anio, paginas, edad_recomendada):
        super().__init__(titulo, autor, anio, paginas)
        self.edad_recomendada = edad_recomendada

    def mostrar(self):
        print(
            f"{self.titulo} — {self.autor} "
            f"({self.anio}) | {self.paginas} páginas | "
            f"Edad recomendada: {self.edad_recomendada} años"
        )

    def es_apto(self, edad_lector):
        return edad_lector >= self.edad_recomendada


# Programa principal

# Objeto de la clase base
libro_comun = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, 96)

# Objeto de la primera subclase
libro_digital = LibroDigital("Clean Code", "Robert C. Martin", 2008, 431, "PDF")

# Objeto de la segunda subclase
libro_infantil = LibroInfantil(
    "Donde viven los monstruos", "Maurice Sendak", 1963, 48, 4
)

# Lista con los tres objetos
biblioteca = [libro_comun, libro_digital, libro_infantil]

# Recorrido de la lista
for libro in biblioteca:
    libro.mostrar()

    if isinstance(libro, LibroInfantil):
        if libro.es_apto(6):
            print("Es apto para un lector de 6 años.")
        else:
            print("No es apto para un lector de 6 años.")
