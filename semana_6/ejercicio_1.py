'''
Determinar si una secuencia de enteros está 
ordenada en forma creciente o
decreciente, o está en desorden. Escriba un 
subprograma para la lectura de los elementos de la
secuencia que lo realice hasta un número N 
especificado por el usuario. No se admite la
secuencia vacía ni unitaria. Luego realice otro 
subprograma que tome la secuencia y vea el tipo
de ordenamiento. Finalice con un subprograma 
que muestre en pantalla el resultado. El programa
principal debe llamar a estos tres subprogramas. 
'''

def read_sequence():
    
    while True:
        try:
            N = int(input("Numero N de la secuencia (N > 1): "))
            if N <= 1:
                raise ValueError("N debe ser mayor a 1")
            break
        except ValueError as e:
            print(e)
    
    sequence = []
    print(f"Introduzca {N} enteros:")
    for _ in range(N):
        while True:
            try:
                num = int(input())
                sequence.append(num)
                break
            except ValueError:
                print("Por favor introduzca un valor valido")
    
    return sequence

def check_order(sequence):
    
    is_increasing = all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1))
    is_decreasing = all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))
    
    if is_increasing:
        return "incremental"
    elif is_decreasing:
        return "decremental"
    else:
        return "desorden"

def display_result(order):
    
    print(f"La secuencia es{order}.")

def main():
    
    sequence = read_sequence()
    order = check_order(sequence)
    display_result(order)

# Llamada a la funcion principal. Main()
if __name__ == "__main__":
    main()

