n1 = int(input("primer entero: "))
n2 = int(input("segundo entero: "))
n3 = int(input("tercer entero: "))

assert(n1 != n2 and n1 != n3 and n2 != n3)
def compare_numbers(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("el numero mayor es: ", n1)
        return n1
    elif n2 > n1 and n2 > n3:
        print("el numero mayor es: ", n2)
        return n2
    elif n3 > n1 and n3 > n2:
        print("el numero mayor es: ", n3)
        return n3
    else:
        print("no se puede saber, n1 n2 y n3 son iguales\n")

compare_numbers(n1,n2,n3)
