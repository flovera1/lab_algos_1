'''
    Has sido contratado por el servicio secreto para trabajar en el área de codificación y
decodificación de ADN. Dado que el equipo de trabajo es bastante grande, a ti solo te
corresponde hacer una pequeña parte del proyecto. Ésta debe ser hecha en Python, y
naturalmente, cumpliendo con todas las buenas prácticas aprendidas hasta ahora: buen estilo
de programación, precondiciones y postcondiciones, invariantes y cotas, análisis descendente
del curso CI-2691 Laboratorio de Algoritmos I.
 Como la cantidad de datos guardados por el servicio secreto es tan grande, los datos
 han sido factorizados para ahorrar espacio. La factorización simplemente consiste en colocar
 un número entero y un string por línea. El número entero indica la cantidad de veces que el
 string debe copiarse para representar la cadena real de ADN. Por ejemplo, una línea que sea
 “3 ACG”, representa a “ACGACGACG”. La cadena solo debe contener los caracteres válidos
 de las bases nitrogenadas ( A, T, C y G ).
  El programa a realizar debe leer un archivo con el formato explicado anteriormente de
  una cadena ADN factorizada, cuyo nombre del archivo es “input.txt”. El programa debe escribir
  en un archivo, el resultado del ADN no-factorizado. El archivo a crear tendrá el nombre
  “output.txt”.
   Como a veces ocurre cuando se almacena información en medios no confiables, los
   datos son susceptibles a errores. Para simplificar el problema, se puede asumir como
   precondición que los números serán no negativos y las cadenas factorizadas de ADN serán no
   mayor a 50 caracteres. Todo lo leído que no cumpla con estas características puede ser
   considerado como un error. En el caso de leer una línea y no posea error, simplemente debe
   imprimir el ADN no-factorizado. Además, el programa debe ser capaz de identificar la líneas
   con los datos erróneos, e imprimir en el resultado el mensaje “Línea errónea”.
    Por ejemplo, si el archivo de entrada contiene:
    1 A
    5 ATCA
    0 CCC
    -1 A
    10 SA
    51 ATCG
    2 T
    La salida correspondiente a dicha entrada es:
    A
    ATCAATCAATCAATCAATCA 
    Linea erronea
    Linea erronea
    Linea erronea
    TT 
'''

# chequear si el string contienen caracteres de ADN valido
def is_valid_dna_string(dna_str):
    valid_charcters = {'A', 'T', 'C', 'G'}
    return all(char in valid_characters for char in dna_str)

# procesa una linea from la entrada input file
def process_line(line):
    try:
        parts = line.strip().split(' ', 1)
        if len(parts) != 2:
            return 'error'
        count = int(parts[0])
        dna_str = parts[1]

        if count < 0 or len(dna_str) > 50 or not is_valid_dna_string(dna_str):
            return 'error'

        return dna_str * count
    except ValueError:
        return 'error'

# leer el archivo de entrada, procesar cada linea y escribir el resultado en un archivo de salida 
def read_and_process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            result = process_line(line)
            outfile.write(result + '\n')

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    read_and_process_file(input_filename, output_filename)

main()





















