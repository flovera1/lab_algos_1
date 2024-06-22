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
    
    while True:
        try:
            N = int(input("Introduzca N para la secuencia (N > 0): "))
            if N <= 0:
                raise ValueError("N debe ser mayor a 0")
            break
        except ValueError as e:
            print(e)
    
    sequence = []
    print(f"Introduzca {N} numeros natural:")
    for _ in range(N):
        while True:
            try:
                num = int(input())
                if num < 0:
                    raise ValueError("Numeros naturales (>= 0).")
                sequence.append(num)
                break
            except ValueError as e:
                print(e)
    
    return sequence

def fibonacci(n):
   
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def produce_fibonacci_sequence(sequence):
    
    return [fibonacci(num) for num in sequence]

def display_sequence(sequence):
    
    print("Fibonacci:")
    for num in sequence:
        print(num, end=' ')
    print()

def main():
    """
    Main
    """
    sequence = read_sequence()
    fibonacci_sequence = produce_fibonacci_sequence(sequence)
    display_sequence(fibonacci_sequence)

# Llamada a la funcion que ejecuta el main
if __name__ == "__main__":
    main()


