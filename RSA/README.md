# 7 RSA

## 7.1. Let the two primes p = 41 and q = 17 be given as set-up parameters for RSA.

1. Which of the parameters e1 = 32, e2 = 49 is a valid RSA exponent? Justify your choice.

Sería 49 ya que phi que es 640 y el número 49 son coprimos

2. Compute the corresponding private key Kpr = (p, q, d). Use the extended Euclidean algorithm for the inversion and point out every calculation step.

[7_1.py](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/RSA/7_1.py)

## 7.2. Computing modular exponentiation efficiently is inevitable for the practicability of RSA. Compute the following exponentiations xe mod m applying the squareand-multiply algorithm:

1. x = 2, e = 79, m = 101
2. x = 3, e = 197, m = 101

After every iteration step, show the exponent of the intermediate result in binarynotation.

[7_2.py](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/RSA/7_2.py)

## 7.3. Encrypt and decrypt by means of the RSA algorithm with the following system parameters:

1. p = 3, q = 11, d = 7, x = 5
2. p = 5, q = 11, e = 3, x = 9

Only use a pocket calculator at this stage.

[7_3.py](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/RSA/7_3.py)

## 7.4. One major drawback of public-key algorithms is that they are relatively slow.
In Sect. 7.5.1 we learned that an acceleration technique is to use short exponents e.
Now we study short exponents in this problem in more detail.

1. Assume that in an implementation of the RSA cryptosystem one modular squar-
ing takes 75% of the time of a modular multiplication. How much quicker is
one encryption on average if instead of a 2048-bit public key the short exponent
e = 216 + 1 is used? Assume that the square-and-multiply algorithm is being used
in both cases.
  -   Supongamos que en una implementación del criptosistema RSA, una operación de cuadrado
      modular toma el 75% del tiempo de una multiplicación modular. Si en lugar de una clave 
      pública de 2048 bits se utiliza el exponente corto e = 2^16 + 1, el cifrado sería
      considerablemente más rápido en promedio debido a que requiere muchas menos operaciones.



2. Most short exponents are of the form e = 2n + 1. Would it be advantageous to
use exponents of the form 2n − 1? Justify your answer.
  -   No sería ventajoso utilizar exponentes de la forma 2n - 1 en RSA. Los exponentes en RSA 
      deben ser coprimos con φ(N), donde N es el módulo del sistema. Si e = 2n - 1, sería un
      número par y, en la mayoría de los casos, no sería coprimo con φ(N), lo que resultaría 
      en una clave pública inválida para RSA.



3. Compute the exponentiation xe mod 29 of x = 5 with both variants of e from
above for n = 4. Use the square-and-multiply algorithm and show each step of
your computation.
  -   Para calcular la exponenciación xe mod 29 de x = 5 con ambas variantes de:
        e (e = 2^16 + 1
        e = 2n + 1 para n = 4)
      puedes utilizar el algoritmo de cuadrado y multiplicación. El proceso implica
      seguir los pasos para cada bit de e y realizar las operaciones correspondientes.

## 7.5. In practice the short exponents e = 3, 17 and 216 + 1 are widely used.

1. Why can’t we use these three short exponents as values for the exponent d in
applications where we want to accelerate decryption?
  -  No podemos usar estos exponentes cortos como d en RSA para descifrar porque sería 
     vulnerable a ataques de fuerza bruta debido a su previsibilidad.

2. Suggest a minimum bit length for the exponent d and explain your answer.
  -  La longitud mínima recomendada para d en RSA es igual o mayor que la longitud de bits 
     del módulo N para garantizar la seguridad y evitar ataques de factorización o fuerza bruta.

## 7.6. Verify the RSA with CRT example in the chapter by computing yd = 15103 mod 143 using the square-and-multiply algorithm.

[7_6.py](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/RSA/7_6.py)

## 7.7. An RSA encryption scheme has the set-up parameters p = 31 and q = 37. The public key is e = 17.

1. Decrypt the ciphertext y = 2 using the CRT.
2. Verify your result by encrypting the plaintext without using the CRT.

[7_7.py](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/RSA/7_7.py)

## 7.8. Popular RSA modulus sizes are 1024, 2048, 3072 and 4092 bit.
1. How many random odd integers do we have to test on average until we expect to
find one that is a prime?
  -  En promedio, debemos probar alrededor de e^N números impares aleatorios para 
     encontrar uno que sea primo, donde N es el tamaño del módulo RSA en bits.

2. Derive a simple formula for any arbitrary RSA modulus size.
  -  La fórmula simple para cualquier tamaño de módulo RSA (N bits) es: Número
     de intentos esperados ≈ e^N.

## 7.9. One of the most attractive applications of public-key algorithms is the establishment of a secure session key for a private-key algorithm such as AES over an insecure channel.
Assume Bob has a pair of public/private keys for the RSA cryptosystem. Develop
a simple protocol using RSA which allows the two parties Alice and Bob to agree
on a shared secret key. Who determines the key in this protocol, Alice, Bob, or both?

    Generación de Claves:
        Bob genera un par de claves RSA: una clave pública (N_B, e_B) y una clave privada (d_B).
        Alice también genera un par de claves RSA: una clave pública (N_A, e_A) y una clave privada (d_A).

    Compartir Clave Pública:
        Bob comparte su clave pública (N_B, e_B) con Alice, y Alice comparte su clave pública (N_A, e_A) con Bob. Esto puede hacerse de manera segura a través de un canal inseguro, ya que las claves públicas no revelan la clave privada.

    Generación de la Clave Compartida:
        Para establecer la clave secreta compartida, cada parte realiza la siguiente operación utilizando su propia clave privada y la clave pública del otro:
            Bob: Calcula la clave compartida K_B = (N_B, e_B) ^ d_B mod N_A
            Alice: Calcula la clave compartida K_A = (N_A, e_A) ^ d_A mod N_B

    Resultado:
        Ahora, tanto Alice como Bob tienen la misma clave secreta compartida, que puede usarse para cifrar y descifrar datos utilizando un algoritmo de cifrado simétrico como AES.

## 7.10. 
In practice, it is sometimes desirable that both communication parties influence the selection of the session key. For instance, this prevents the other party from choosing a key which is a weak key for a symmetric algorithm. Many block ciphers such as DES and IDEA have weak keys. Messages encrypted with weak keys can be recovered relatively easily from the ciphertext. Develop a protocol similar to the one above in which both parties influence the
key. Assume that both Alice and Bob have a pair of public/private keys for the RSA cryptosystem. Please note that there are several valid approaches to this problem.

Show just one.

    Generación de Claves:
        Bob genera un par de claves RSA: una clave pública (N_B, e_B) y una clave privada (d_B).
        Alice también genera un par de claves RSA: una clave pública (N_A, e_A) y una clave privada (d_A).

    Compartir Clave Pública y Sesión Aleatoria:
        Bob comparte su clave pública (N_B, e_B) con Alice, y Alice comparte su clave pública (N_A, e_A) con Bob.
        Ambos participantes generan una cadena de bits aleatoria de la misma longitud que la clave de sesión deseada, que llamaremos "K_random".

    Mezcla de las Cadenas Aleatorias:

        Tanto Alice como Bob mezclan sus cadenas aleatorias generadas (K_random) utilizando una operación XOR. Esto significa que cada uno influye en la formación de la clave de sesión secreta sin que el otro pueda predecirla.
            Alice: Calcula K_mix = K_random ^ K_B
            Bob: Calcula K_mix = K_random ^ K_A

    Aquí, "^" representa la operación XOR entre las cadenas de bits.

    Resultado:
        Ahora, ambos tienen la misma clave de sesión secreta K_mix, que es el resultado de la mezcla de sus cadenas aleatorias. Esta clave puede usarse para cifrar y descifrar datos utilizando un algoritmo de cifrado simétrico como AES.

## 7.11 

In this exercise, you are asked to attack an RSA encrypted message. Imagine
being the attacker: You obtain the ciphertext y = 1141 by eavesdropping on a certain
connection. The public key is k pub = (n, e) = (2623, 2111).
1. Consider the encryption formula. All variables except the plaintext x are known.
Why can’t you simply solve the equation for x?
  -  No puedes resolver la ecuación para x porque no conoces el valor de n, que es el
     módulo utilizado en RSA, y factorizar n es computacionalmente difícil.


2. In order to determine the private key d, you have to calculate d ≡ e−1 mod Φ (n).
There is an efficient expression for calculating Φ (n). Can we use this formula
here?
  -  La fórmula eficiente para calcular Φ(n) requiere conocer los valores de p y q,
     que no están disponibles en este escenario.


3. Calculate the plaintext x by computing the private key d through factoring n =
p · q. Does this approach remain suitable for numbers with a length of 1024 bit
or more?
  -  La factorización de n se vuelve extremadamente difícil a medida que el tamaño de
     n aumenta, y para números RSA de 1024 bits o más, puede ser prácticamente imposible 
     de realizar en un tiempo razonable.

## 7.12. We now show how an attack with chosen ciphertext can be used to break an RSA encryption.
1. Show that the multiplicative property holds for RSA, i.e., show that the product
of two ciphertexts is equal to the encryption of the product of the two respective
plaintexts
  -  La propiedad multiplicativa se cumple en el cifrado RSA, lo que significa que el producto 
     de dos textos cifrados es igual a la encriptación del producto de los dos textos originales 
     correspondientes.


2. This property can under certain circumstances lead to an attack. Assume that
Bob first receives an encrypted message y1 from Alice which Oscar obtains by
eavesdropping. At a later point in time, we assume that Oscar can send an inno-
cent looking ciphertext y2 to Bob, and that Oscar can obtain the decryption of y2 .
In practice this could, for instance, happen if Oscar manages to hack into Bob’s
system such that he can get access to decrypted plaintext for a limited period of
time.
  -  Esta propiedad puede llevar a una situación de ataque en la que un espía, Oscar, 
     puede enviar un texto cifrado que parece inocente (y2) a Bob después de interceptar 
     un mensaje cifrado (y1) de Alice. Oscar puede entonces obtener la desencriptación de y2, 
     posiblemente mediante la intrusión en el sistema de Bob para acceder a los textos originales 
     durante un tiempo limitado.    

## 7.13 Exploits

In this exercise, we illustrate the problem of using nonprobabilistic cryptosys-
tems, such as schoolbook RSA, imprudently. Nonprobabilistic means that the same
sequence of plaintext letters maps to the same ciphertext. This allows traffic analysis
(i.e., to draw some conclusion about the cleartext by merely observing the cipher-
text) and in some cases even to the total break of the cryptoystem. The latter holds
especially if the number of possible plaintexts is small. Suppose the following situ-
ation:
Alice wants to send a message to Bob encrypted with his public key pair (n, e).
Therefore, she decides to use the ASCII table to assign a number to each character
(Space → 32, ! → 33, . . . , A → 65, B → 66, . . . , ∼→ 126) and to encrypt them
separately.

1. Oscar eavesdrops on the transferred ciphertext. Describe how he can successfully
decrypt the message by exploiting the nonprobabilistic property of RSA.
  -  Oscar puede descifrar con éxito el mensaje explotando la propiedad no probabilística
     de RSA de la siguiente manera:
        - Él sabe que cada carácter se cifra por separado, por lo que podria identificar los
          valores ASCII de los caracteres individuales en el texto cifrado.
        - Dado que RSA es determinista (no probabilístico), el mismo valor de texto sin formato
          siempre producirá el mismo valor de texto cifrado. Oscar puede utilizar una simple búsqueda
          en una tabla para hacer coincidir los valores de texto cifrado con sus correspondientes valores
          ASCII de texto sin formato.
        - Una vez que Oscar haya determinado los valores ASCII de todos los caracteres en el texto cifrado,
          puede convertirlos nuevamente en caracteres según la tabla ASCII para revelar el mensaje original.



2. Bob’s RSA public key is (n, e) = (3763, 11). Decrypt the ciphertext
y = 2514, 1125, 333, 3696, 2514, 2929, 3368, 2514
with the attack proposed in 1. For simplification, assume that Alice only chose
capital letters A–Z during the encryption.
  -  Utilizando la clave pública de Bob (n, e) = (3763, 11) y el ataque descrito anteriormente
     Oscar puede descifrar el texto cifrado y = 2514, 1125, 333, 3696, 2514, 2929, 3368, 2514 para
     revelar el mensaje.

3. Is the attack still possible if we use the OAEP padding? Exactly explain your
answer.
  -  Si se utiliza el relleno OAEP (Optimal Asymmetric Encryption Padding), el ataque
     descrito en el punto 1 no sería posible. OAEP está diseñado para agregar relleno
     probabilístico al texto sin formato antes de cifrarlo, lo que garantiza que el mismo
     texto sin formato no produzca el mismo texto cifrado.

     https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding

## 7.14 Attacks

 The modulus of RSA has been enlarged over the years in order to thwart im-
proved attacks. As one would assume, public-key algorithms become slower as the
modulus length increases. We study the relation between modulus length and perfor-
mance in this problem. The performance of RSA, and of almost any other public-key
algorithm, is dependent on how fast modulo exponentiation with large numbers can
be performed.

Supongamos que una multiplicación o elevación al cuadrado de módulo con
números de k bits toma c · k^2 ciclos de reloj, donde c es una constante.
Si solo se considera el cifrado/descifrado en sí con un exponente de longitud
 completa y el algoritmo de elevar al cuadrado y multiplicar.

Para comparar el cifrado/descifrado RSA con 1024 bits y RSA con 512 bits,
podemos calcular la relación entre sus tiempos en función del tamaño de los
números (bits). Supongamos que t_1024 es el tiempo en ciclos de reloj para
operaciones RSA con 1024 bits y t_512 es el tiempo en ciclos de reloj para
operaciones RSA con 512 bits. Entonces, la relación de velocidad sería:

(t_1024 / t_512) = ((c * 1024^2) / (c * 512^2))

La constante 'c' se cancela y podemos simplificar la expresión:

(t_1024 / t_512) = (1024^2 / 512^2) = (2^20 / 2^18) = 2^2 = 4

Por lo tanto, en promedio, RSA con 1024 bits es aproximadamente 4
veces más lento que RSA con 512 bits utilizando el algoritmo de
elevar al cuadrado y multiplicar.
    
En la práctica, el algoritmo de Karatsuba se utiliza a menudo para la multiplicación
de números largos en criptografía, y su complejidad asintótica es proporcional a k log2 3.
Supongamos que esta técnica más avanzada requiere c · k log2 3 = c · k^1.585 ciclos de reloj
 para la multiplicación o la elevación al cuadrado, donde c es una constante. Nuevamente
podemos emplear algo parecido para determinar el tiempo de ejecución en el algoritmo de Karatsuba

(t_1024 / t_512) = ((c * 1024^1.585) / (c * 512^1.585))

La constante 'c' se cancela y podemos simplificar la expresión:

(t_1024 / t_512) = (1024^1.585 / 512^1.585)

Para calcular esto exactamente, necesitaríamos conocer el valor exacto de la constante 'c' para el
algoritmo de Karatsuba. Sin embargo, podemos decir que si el algoritmo de Karatsuba es más eficiente
que el algoritmo estándar (c * k^2), entonces la relación t_1024 / t_512 será menor que 4. Es decir,
RSA con 1024 bits será más rápido en comparación con RSA con 512 bits cuando se utiliza el algoritmo
 de Karatsuba. La cantidad exacta dependerá de los valores específicos de 'c' para cada algoritmo.
