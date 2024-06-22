'''
calcula la suma de todos los elementos de una matriz N×M. El programa solicitará al usuario que ingrese las dimensiones de la matriz y luego los elementos de la matriz.
'''

def main():
    # tomar las dimensiones de la matriz del usuario
    N = int(input("introduce el numero de filas N: "))
    M = int(input("introduce el numero de columnas M: "))

    matrix = []

    # leer los elementos de la matriz por parte del usuario
    print("intriduce los elementos de la matriz fila por fila")
    for i in range(N):
        row = []
        for j in range(M):
            elemento = float(input(f"elemento en la posicion({i+1}, {j+1}): "))
            row.append(elemento)
        matrix.append(row)
    # calcular la suma de los elementos de la matriz

    total_sum = 0
    for row in matrix:
        total_sum += sum(row)

    print(f"la suma de los elementos es: {total_sum}")

main()
