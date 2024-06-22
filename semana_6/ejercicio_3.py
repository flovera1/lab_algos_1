'''Dado dos números naturales N y M, escriba un programa que produzca la lista
de los factores primos de M que son menores o iguales a N.. Se sugiere que utilice el mismo
esquema de análisis descendente de los otros dos ejercicios. Además, puede escribir una función
que determine si un número es primo; y otra que dado un natural X diga si divide a otro natural Y.
Con estas dos funciones puede determinar cuáles números primos dividen a M'''

def read_inputs():
    =
    while True:
        try:
            N = int(input("Enter a natural number N (N > 0): "))
            if N <= 0:
                raise ValueError("N must be a natural number greater than 0.")
            M = int(input("Enter a natural number M (M > 0): "))
            if M <= 0:
                raise ValueError("M must be a natural number greater than 0.")
            break
        except ValueError as e:
            print(e)
    
    return N, M

def is_prime(num):
    
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_divisible(x, y):
    
    return y % x == 0

def find_prime_factors(N, M):
    
    prime_factors = []
    for i in range(2, N + 1):
        if is_prime(i) and is_divisible(i, M):
            prime_factors.append(i)
    return prime_factors

def display_result(prime_factors):
    
    if prime_factors:
        print("Prime factors of M that are <= N:", prime_factors)
    else:
        print("There are no prime factors of M that are <= N.")

def main():
    
    N, M = read_inputs()
    prime_factors = find_prime_factors(N, M)
    display_result(prime_factors)

# Call the main function to execute the program
if __name__ == "__main__":
    main()

