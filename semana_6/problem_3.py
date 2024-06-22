'''
Dado dos números naturales N y M, escriba un programa que produzca la lista
de los factores primos de M que son menores o iguales a N.. Se sugiere que utilice el mismo
esquema de análisis descendente de los otros dos ejercicios. Además, puede escribir una función
que determine si un número es primo; y otra que dado un natural X diga si divide a otro natural Y.
Con estas dos funciones puede determinar cuáles números primos dividen a M
'''
def read_inputs():
    """
    Reads two natural numbers N and M from the user.
    Returns the numbers as a tuple (N, M).
    """
    while True:
        try:
            N = int(input("Entre N N (N > 0): "))
            if N <= 0:
                raise ValueError("N > 0.")
            M = int(input("Entre M (M > 0): "))
            if M <= 0:
                raise ValueError("M > 0")
            break
        except ValueError as e:
            print(e)

    return N, M

def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def es_divisible (x, y):
    '''
        determina si x divide a y.
        Devuelve True si x divide a y , False si no
    '''
    return y % x == 0


def encontrar_factores_primos(N, M):
    '''
        Encuentra factores primos de M que son menores o iguales a N.
        Devuelve una lista de estos factores
    '''
    factores_primos = []
    for i in range(2, N + 1):
        if es_primo(i) and es_divisible(i, M):
            factores_primos.append(i)

    return factores_primos


def muestra_resultados(factores_primos):
    '''
        Muestra la lista de factores primos
    '''
    if factores_primos:
        print("factores primos de M que son menores o iguales a N: ", factores_primos)
    else:
        print("No hay factores primos de M que sean menores o iguales a N")


def main():

    N, M = read_inputs()
    factores_primos = encontrar_factores_primos(N, M)
    muestra_resultados(factores_primos)

main()

















