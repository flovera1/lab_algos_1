# crear un programa que lee los coeficientes de un polinomio,
# los almacena un arreglo y lo muestra en notacion de polinomio
# el programa asegura que el grado del polinomio no se excede de
# un entero M que es dado por el usuario


# Cosas para aprender / EXPLICACION:

# 1) Inicializacion: El programa empieza pidiendo al usuario que introduzca
# el valor del entero M. El grado del polinomio

# 2) Leer los coeficientes: Entramos en un loop que lee coeficientes del 
# polinomio

# 3) Grado del polinomio, determinado por los coeficientes del polinomio
# 4) Mostrar los resultados.







def coeficientes():
    # preguntar por el valor de M
    M = input("The grado de max del polinomio (M): ")
    # inicializacion de una lista vacia
    coeficientes = []
    # leer los coeficientes del usuario desde 0 hasta M
    print(f"Introduzca los coeficientes del polinomio (hasta un grado M)")

    while(len(coeficientes) <= int(M)):
        coeff = float(input(f"Introduzca coeficiente para X^{len(coeficientes):}"))
        if coeff == 0 and len(coeficientes) > 0:
            break
        coeficientes.append(coeff)

    # Determinar el grado del polinomio
    grado = len(coeficientes) - 1

    # 
    print(f"El grado del polinomio es: {grado}")
    # construir el polinomio en notacion de string

    polinomio = "P(X) = "
    terminos = []
    for i, coeff in enumerate(coeficientes):
        if i == 0:
            terminos.append(f"{coeff}")
        else:
            terminos.append(f"{coeff}X^{i}")
    polinomio += " + ".join(terminos)

    # 
    print(polinomio)
#coeficientes()


# programa que almacena 10 enteros y los suma
def suma_10_enteros():
    lista = [] # se guardan los valores a sumar
    sumatoria = 0 # variable donde se guarda el valor de la sumatoria

    # FOR loop para pedir los digitos
    for i in range(1, 11):
        lista.append(int(input("Introduzca el valor del numero " + str(i) + ": ")))

    # PRE. verificar que ese valor sea entero
    assert(all(x for x in lista if type(x) == int and x != 0))

    # FOR loop para la sumatoria
    for i in lista:
        sumatoria += i

    # POST. verificar que la suma sea la sumatoria correcta
    assert(sumatoria == sum(x for x in lista))
    
    return sumatoria

#print(suma_10_enteros())





# Clases en Python 

# Que es una clase?
# Una clase es una abstraccion del mundo real
# Es un representacion de algo. Por ejemplo una clase puede ser "edificio"
# "universidad", etc...
# Es el ente mas general.

# clase comida:
'''
class comida:
    nombre = "arepa"
    carga_calorias = 350
    sabor = "queso con aguacate"

# avila burger
# Programa que se encargue de verificar el ganador de una competencia 
# de quien come mas hamburguesas

class competidor():
    nombre = ""
    hamburguesas = 0

lista = [competidor(), competidor(), competidor(), competidor(), competidor()]

# FOR loop que itere en la lista de participantes, pidiendo el nombre y el numero de hamburgesas

for estudiante in range(0,5):
    lista[estudiante].nombre = input("\n Nombre del concursante: ")
    lista[estudiante].hamburguesas = int(input("\nNumero de hamburguesas comidas:"))
    # verificar que el nombre tenga al menos 1 caracter

# PRE. Verificar que el numero de hamburguesas de cada participante sea un numero positivi
assert(all(lista[i].hamburguesas >= 0 for i in range(0,5)))

#ordenamos la lista de mayor a menor
lista = sorted(lista, key = lambda competidor: competidor.hamburguesas, reverse = True)

# POST. verificar que de primera posicion este el concursante que posea
# mayor numero de hamburguesa y asi mismo con la siguiente posicion respecto
# a la siguiente

assert(all(lista[x].hamburguesas >= lista[x + 1].hamburguesas for x in range(0, 4)))
# salida

for i in range(0, 5):
    print(lista[i].nombre + " con "+ str(lista[i].hamburguesas) + "")


'''

# programa que calcule el promedio de edades sy de indice de un grupo de N estudiantes

# variables

suma_indice = 0
suma_edad = 0
promedio_edad = 0
promedio_indice = 0

# clase de estudiantes

class estudiante():
    nombre = ""
    indice = ""
    edad = ""


N = int(input("introduzca el numero de estudiantes que posee el grupo: "))

# PRE. el numero de estudiantes sea mayor a 1
assert(N > 1)

# Arreglo de estudiantes

grupo = [estudiante() for x in range(N)]

# FOR loop para introducir datos del grupo de estudiantes

for x in range(N):
    grupo[x].nombre = input("\nNombre del estudiante " + str(x) + "? ")
    grupo[x].indice = float(input("\nindice del estudiante " + str(x) + "? "))
    grupo[x].edad = int(input("\nedad del estudiante" + str(x) + "? "))
    # verificamos que el nombre tenga al menos un caracter
    # que el indice y la edad sean positivos
    assert(len(grupo[x].nombre) >= 1 and grupo[x].edad > 0 and grupo[x].indice > 0)



# promedio de las edades
for y in range(N):
    suma_edad +=grupo[y].edad
promedio_edad = suma_edad/N

# promedio los indices
for z in range(N):
    suma_indice += grupo[z].indice
promedio_indice = suma_indice /N

# POST. verificar q la sumatoria de edades y de indices sea correcta

assert(promedio_edad == sum(grupo[x].edad for x in range(N))/N and promedio_indice == sum(grupo[x].indice for x in range(N))/N)









print("promedio: " + str(promedio_edad))
print("indice: " + str(promedio_indice))














