# algoritmo q calcula la suma de los factoriales desde 0 hasta N.
# recuerde que 0!= 1
#
# ejemplo: N = 5 entonces la suma de los factoriales: 0! + 1! + 2! + 3! + 4! =# 34
'''
const N : int;
var suma: int;
var fact: int;
var k: int;

{N >= 0}
suma, fact, k:=0,1,0;

{N >= 0 ^ 0<=k<=N}
do (k <=N ) ->
    if (k > 0) ->
        fact := fact * k
    []
        skip;
    fi
    suma := suma + fact;
    k := k + 1
od

{suma = (sumatoria i: 0<=i<=N )}
'''
# valores iniciales:
# N: representando el numero q deseamos trabajar: int
# k: valor que se usa para iterar
# fact: es el factorial del numero que se iterando
# suma: todos los factoriales sumados
'''
N = int(input("algoritmo que calcula la suma de todos los factoriales hasta(N):\n"))
suma, fact, k = 0, 1, 0

# pre:
assert(N >= 0 and 0<=k<=N)

# loop, calcula la sumatoria de los factoriales
while k<= N:
    if (k > 0):
        fact = fact * k
        # fact *= k calcular el factorial del numero que estamos iterando
    suma = suma + fact
    # suma += fact
    k = k +1
    # k += 1

print(suma)




# definir una funcion que haga la productoria de un conjunto de numeros:

def prod(conjunto):
    p = 1
    for n in conjunto:
        p *= n
    return p

print(prod([1,2,3,4,5]))

'''


'''
Hacer un algoritmo que calcula la suma de los digitos de un numero entero N
de 10 digitos maximo

GCL:
    conts N: int;
    var suma: int;
    var cociente: int;

    {N > 0}
    suma, cociente:= 0, N;

    do (cociente > 0) ->
        suma := suma + cociente mod 10
        cociente := coiente dive 10
    od


'''
# importamos la bibliote sys
import sys
N = int(sys.argv[1])
suma, cociente = 0, N
# precondicion:
assert(0<N<10000000000)
# algoritmo:
while(cociente > 0):
    suma = suma + (cociente%10)
    cociente = cociente // 10

print(suma)
assert(suma == sum((N // (10**(i)))%10 for i in range(0, 11) if (N//(10**(i))!= 0)))



































