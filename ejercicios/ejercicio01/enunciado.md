Ejercicio 1 — Clasificación de temperatura 

Una estación meteorológica registra una temperatura ingresada por el usuario.

El programa debe:

- pedir una temperatura (número entero)
- indicar si es:
    - bajo cero (menor a 0)
    - templada (entre 0 y 25)
    - alta (mayor a 25)

 Extensión: validar que el dato ingresado sea numérico.

<
>
<=
>=
==
!=  

Pedir temperatura al usuario
Intentar convertirla a número entero

Si no se puede convertir:
    Mostrar mensaje de error

Si se puede convertir:
    Si temperatura < 0:
        Es bajo cero
    Si temperatura está entre 0 y 25:
        Es templada
    Si temperatura > 25:
        Es alta

Prueba..