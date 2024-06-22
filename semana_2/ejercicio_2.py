'''[
const esDescendienteExtranjero : bool;
const edad : int;
var puedeVotar: bool;
{ 0 < edad < 120 }
puedeVotar:= true;
if ( esDescendienteExtranjero )
Tú
14:00
puedeVotar:= true;
if ( esDescendienteExtranjero ) ­>
   if ( edad >= 25 ) ­>
      skip;
   [] ( edad < 25 )
      puedeVotar = False;
[] ( ! esDescendienteExtranjero ) ­>
   if ( edad >= 18 ) ­>
      skip;
   [] ( edad < 18 )
      puedeVotar = False;
fi
{ postcondición ...}

]'''
puede_votar = False

es_extranjero = int(input("es extranjero (0 o 1)?"))
edad = int(input("introduzca su edad: "))
puede_votar = False
#print("es extranjero?", es_extranjero)
if es_extranjero == 1:
    if edad >= 25:
        puede_votar = True
    else:
        puede_votar = False
else:
    # no es descendiente de extranjero
    if edad >= 18:
        puede_votar = True
    else:
        puede_votar = False

if puede_votar:
    print("Si puedes votar")
else:
    print("No puedes votar")
assert(puede_votar == True or puede_votar == False)


# hacer casting
