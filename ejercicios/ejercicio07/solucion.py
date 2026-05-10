notas = []
contador = 0

for i in range(5):

    nota = float(input("Igresar Nota: "))

    notas.append(nota)


print(f"Notas cargadas: {notas} ")

for nota in notas:

    if nota >= 6:

        contador = contador + 1

print(f"Cantidad de notas mayores o iguales a 6: {contador}")
