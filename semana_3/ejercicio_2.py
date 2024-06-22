'''
algoritmo que calcula la suma de los factoriales desde 0 hasta N.
Rcuerde que 0!=1.
[
const N: int;
var suma: int;
var fact: int;
var k: int;
{N >= 0}
suma,fact,k := 0,1,0;
{ N >= 0 ∧ 0<=k<=N }
do ( k<=N ) ->
if ( k > 0 ) ->
fact := fact * k
[]
skip;
fi;
suma := suma + fact;
k := k + 1
od
{ suma = (∑ 𝑖: 0<=i<=N: (∏j: 1<=j<=i: j)) }
]
'''