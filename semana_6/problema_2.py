'''
Dado un número N se debe leer una secuencia de N 
números naturales y los
almacene en un arreglo. El programa debe producir 
una secuencia con el número de Fibonacci
de cada uno de los números de la entrada. Utilice 
el mismo esquema de la pregunta anterior: un
subprograma para la lectura de la secuencia, otro 
para producir los números de Fibonacci en un
segundo arreglo y otro que tome este segundo 
arreglo y lo imprima en pantalla. Sugerencia:
    escriba una función que dado un número natural i 
    produzca el número Fibonacci fib(i) de dicho
    valor. 
'''

def read_sequence():
    """
    Reads a sequence of N natural numbers from the user.
    Returns the sequence as a list of integers.
    """
    while True:
        try:
            N = int(input("Enter the number of elements in the sequence (N > 0): "))
            if N <= 0:
                raise ValueError("N must be greater than 0")
            break
        except ValueError as e:
            print(e)

    sequence = []
    print(f"Enter {N} natural numbers:")
    for _ in range(N):
        while True:
            try:
                num = int(input())
                if num < 0:
                    raise ValueError("Number must be a natural number (>= 0).")
                sequence.append(num)
                break
            except ValueError as e:
                print(e)

    return sequence


def fibonacci(n):
    '''
        computa el numero de fibonacci de un numbero natural
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def producir_fibo(secuencia):
    '''
        produce una secuencia de numeros de fibonacci para la
        secuencia secuencia pasada como parametro
    '''
    return [fibonacci(num) for num in secuencia]



def muestre_secuencia(secuencia):
    """
    mostrar la secuencia
    """
    print("Secuencia de fibonacci")
    for num in secuencia:
        print(num)
    print()



def main():
    secuencia = read_sequence()
    fibonacci_sequence = producir_fibo(secuencia)
    muestre_secuencia(fibonacci_sequence)

main()

