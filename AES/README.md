# AES (Advanced Encryption Standard)

## 4.1 Introducción
Desde el 26 de mayo de 2002, el AES (Advanced Encryption Standard) describe el estándar oficial del gobierno de los Estados Unidos.

### 1. Historia Evolutiva de AES
La historia evolutiva de AES difiere significativamente de la de DES. AES, más conocido como Rijndael, es un esquema de cifrado que fue el resultado de un concurso llevado a cabo por el NIST en 1997, en el que participaron criptógrafos de todo el mundo y concluyó en 2001. Por otro lado, DES fue un algoritmo desarrollado por IBM con contribuciones de la NSA y está basado en la estructura de Feistel.

### 2. Eventos Fundamentales en el Proceso de Desarrollo
- En 1997, el NIST anuncia el proceso de selección para AES.
- En 1998, se anuncian los 15 algoritmos admitidos en la primera conferencia de AES.
- En 1999, se escogen los 5 finalistas, tras discutir y someterlos a análisis, en la segunda conferencia de AES.
- En el año 2000, se votó cuál sería el algoritmo a utilizar, donde RIJNDAEL fue el ganador.
- En 2001, se impone como estándar el RIJNDAEL, cambiando su nombre a AES.

### 3. Nombre del Algoritmo
El algoritmo conocido como AES se llamaba originalmente RIJNDAEL.

### 4. Desarrolladores del Algoritmo
Este algoritmo fue desarrollado por dos estudiantes de la Katholieke Universiteit Leuven, Joan Daemen y Vincent Rijmen.

### 5. Tamaños de Bloque y Longitudes de Clave Soportadas
- Tamaño de bloque: 128 bits.
- Longitudes de clave soportadas: 128, 192 y 256 bits.

## 4.2 Galois Field

For the AES algorithm, some computations are done by Galois Fields (GF).
With the following problems, we practice some basic computations.
Compute the multiplication and addition table for the prime field GF(7). A multiplication table is a square (here: 7 × 7) table which has as its rows and columns all field elements. Its entries are the products of the field element at the corresponding row and column. Note that the table is symmetric along the diagonal. The addition table is completely analogous but contains the sums of field elements as entries.

[4_2.py](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/AES/4_2.py)

## 4.4 Addition

Addition in GF(24 ): Compute A(x) + B(x) mod P(x) in GF(24 ) using the ir-
reducible polynomial P(x) = x4 + x + 1. What is the influence of the choice of the
reduction polynomial on the computation?
1. A(x) = x2 + 1, B(x) = x3 + x2 + 1
  -  Al estar en un rango de GF(2), tratamos los numeros como un conjunto binario (1+0=1, 1+1=0)
     a lo que podriamos resolver esto como una suma de polinomios normal:
  = (x² + 1) + (x³ + x² + 1)
  = (0x³ + 1x³) + (1x² + 1x²) + (1 + 1)
  = 1 + 0 + 0
  = x³ 
     Por lo que nuestro resultado es x³

2. A(x) = x2 + 1, B(x) = x + 1
  = (x² + 1) + (x + 1)
  = 1 + 1= 0
  = x² + x

## 4.6 GF

Compute in GF(2⁸):
(x⁴ + x + 1)/(x⁷ + x⁶ + x³ + x² ),
where the irreducible polynomial is the one used by AES, P(x) = x⁸ +x⁴ +x³ + x + 1.
Note that Table 4.2 contains a list of all multiplicative inverses for this field.

Del denominador, obtenemos la transformación binaria:
  x⁷+ x⁶ + x³ + x²
Donde un multiplicador 1 será 1 y un 0 será 0:
  1100 1100 = CC
Convertido a hexadecimal, buscaremos su multiplicativo inverso en la tabla 4.2:
  1B = 0001 1011
Lo convertimos a binario y multiplicamos el resultado por el numerador 
  x⁵+x⁴+x²+x * x⁴+x+1 = x⁹+x⁸+x⁵+x⁴+x³+x = Q
Ya habiendo aplicado el espacio manejado en GF(2), le aplicamos el modulo dividiendo entre P

Q MOD P = x⁴+x²+x+1

## 4.8 Polinomios

Find all irreducible polynomials
1. of degree 3 over GF(2),
2. of degree 4 over GF(2).
The best approach for doing this is to consider all polynomials of lower degree and
check whether they are factors. Please note that we only consider monic irreducible
polynomials, i.e., polynomials with the highest coefficient equal to one.

Primero debemos canonizar el estandar de los polinomios irreducibles donde:
a, b, y c pueden ser 1 y 0.
x³+ax²+bx+1
x⁴+ax³+bx²+cx+1

Para los valores de grado 3 serian:
x³+1x²+0x+1 = x³+x²+1
x³+0x²+1x+1 = x³+x+1

Para los valores de grado 4, se debe ser un poco mas selectivo, puesto que se debe analizar
que ninguno de sus polinomios sea un producto de polinomios de grado menor:

x⁴+0x³+0x²+0x+1 = x⁴+1         -> Puede factorizarse
x⁴+0x³+0x²+1x+1 = x⁴+x+1       -> No puede factorizarse en polinomios menores
x⁴+0x³+1x²+0x+1 = x⁴+x²+1      -> Puede factorizarse
x⁴+0x³+1x²+1x+1 = x⁴+x²+x+1    -> Puede factorizarse
x⁴+1x³+0x²+0x+1 = x⁴+x³+1      -> No puede factorizarse en polinomios menores 
x⁴+1x³+0x²+1x+1 = x⁴+x³+x+1    -> No puede factorizarse en polinomios menores
x⁴+1x³+1x²+0x+1 = x⁴+x³+x²+1   -> Puede factorizarse
x⁴+1x³+1x²+1x+1 = x⁴+x³+x²+x+1 -> No puede factorizarse en polinomios menores

## 4.10 AES columns

In the following, we check the diffusion properties of AES after a sin-
gle round. Let W = (w 0 , w 1 , w 2 , w 3 ) = (0x01000000, 0x00000000, 0x00000000,
0x00000000) be the input in 32-bit chunks to a 128-bit AES. The subkeys for the
computation of the result of the first round of AES are W 0 , . . . ,W 7 with 32 bits each
are given by
W 0 = (0x2B7E1516),
W 1 = (0x28AED2A6),
W 2 = (0xABF71588),
W 3 = (0x09CF4F3C),
W 4 = (0xA0FAFE17),
W 5 = (0x88542CB1),
W 6 = (0x23A33939),
W 7 = (0x2A6C7605).
Use this book to figure out how the input is processed in the first round (e.g., S-
Boxes). For the solution, you might also want to write a short computer program or
use an existing one. In any case, indicate all intermediate steps for the computation
of ShiftRows, SubBytes and MixColumns!
1. Compute the output of the first round of AES to the input W and the subkeys
W 0 , . . . ,W 7 .
2. Compute the output of the first round of AES for the case that all input bits are
zero.
3. How many output bits have changed? Remark that we only consider a single
round — after every further round, more output bits will be affected (avalanche effect).

[4_10.py](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/AES/4_10.py)


