n = int(input("Introduce un anio: "))

if n%4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("El anio es bisiesto")
        else:
            print("El anio no es bisiesto")
    else:
        print("El anio no es bisiesto")
else:
    print("El anio no es bisiesto")
