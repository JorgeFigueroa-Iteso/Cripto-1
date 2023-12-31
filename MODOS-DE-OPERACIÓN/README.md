# Sección 5

## Ejercicio 5.1
### **Consider the storage of data in encrypted form in a large database using AES.**
 1. One record has a size of 16 bytes. Assume that the records are not related to one another. Which mode would be best suited and why?
 2. La modalidad de cifrado en cadena de bloques (CBC) no es apropiada ya que queremos poder acceder a registros individuales de forma aleatoria. Para este caso de uso muy simple, el modo de Libro de Códigos Electrónicos (ECB) probablemente sea el más apropiado, aunque podremos ver si dos registros son iguales. Esto podría solucionarse potencialmente utilizando algún tipo de sal si esto es un problema.

## Ejercicio 5.2
### **We consider known-plaintext attacks on block ciphers by means of an exhaustive key search where the key is k bits long. The block length counts n bits with n > k.**
1. **How many plaintexts and ciphertexts are needed to successfully break a block cipher running in ECB mode? How many steps are done in the worst case?**
- Depende del nivel de confianza con el que estés satisfecho. Dado que la longitud de la clave es menor en bits que la longitud del bloque, es posible (por el principio de las palomas en el agujero) que cada clave se mapee a un único texto cifrado. Sin embargo, no es seguro. Para un determinado texto plano, puede haber múltiples claves que se mapeen al mismo texto cifrado.

2. **Assume that the initialization vector IV for running the considered block cipher in CBC mode is known. How many plaintexts and ciphertexts are now needed to break the cipher by performing an exhaustive key search? How many steps need now maximally be done? Briefly describe the attack.**
- Depende del nivel de confianza con el que estés satisfecho. Dado que la longitud de la clave es menor en bits que la longitud del bloque, es posible (por el principio de las palomas en el agujero) que cada clave se mapee a un único texto cifrado. Sin embargo, no es seguro. Para un determinado texto plano, puede haber múltiples claves que se mapeen al mismo texto cifrado.

3. **How many plaintexts and ciphertexts are necessary, if you do not know the IV?**
- Depende del nivel de confianza con el que estés satisfecho. 
Dado que la longitud de la clave es menor en bits que la longitud del bloque, es posible (por el principio del palomar) que cada clave se mapee a un único texto cifrado. 
Sin embargo, no es seguro. Para un determinado texto plano, puede haber múltiples claves que se mapeen al mismo texto cifrado. Dependiendo de los valores reales de k y n, tener un segundo par (texto plano, texto cifrado) puede proporcionar un alto grado de certeza. Esto se debe a que es poco probable que la clave falsa también se mapee al mismo texto cifrado para otro texto plano. Para calcular la probabilidad de encontrar una clave falsa positiva (donde t es el número de textos planos elegidos que tienes), puedes usar esta fórmula:<br /><br /> 2k-tn. <br /><br />En el peor de los casos (que la última clave verificada de todas las posibles sea la correcta), tendrás que realizar 2k verificaciones.

4. **Is breaking a block cipher in CBC mode by means of an exhaustive key search considerably more difficult than breaking an ECB mode block cipher?**
- Romper un cifrado en modo CBC no es tan costoso como romper un cifrado en modo ECB.<br/> Si el IV se conoce, romper un cifrado en modo CBC es equivalente a romper un cifrado en modo ECB.

## Ejercicio 5.3
### **In a company, all files which are sent on the network are automatically encrypted by using AES-128 in CBC mode. A fixed key is used, and the IV is changed once per day. The network encryption is file-based, so that the IV is used at the beginning of every file.**
- **You managed to spy out the fixed AES-128 key, but do not know the recent IV.<br/> Today, you were able to eavesdrop two different files, one with unidentified content and one which is known to be an automatically generated temporary file and only contains the value 0xFF. Briefly describe how it is possible to obtain the unknown initialization vector and how you are able to determine the content of the unknown file.**
### OBJETIVO
- Obtener el IV desconocido
### PASOS
1. Determinar IV
 - Al tener el archivo "temporal" sabemos que contiene 0xFF. En CBC podemos descifrar el primer bloque:
    - C1 = E<sub>k</sub> (P XOR IV)
    - Sabemos que P = 0xFF y C1 (del archivo interceptado) = 0x1F
    - IV=P XOR D<sub>k</sub>(C<sub>1</sub>)
    - D<sub>k</sub> = Función de decremento usando la "llave" k.

2. Desencriptar el archivo desconocido
 - P<sub>i</sub> = D<sub>k</sub>(C<sub>i</sub>) XOR C<sub>i-1</sub> (for i > 1)
 - P<sub>1</sub> = D<sub>k</sub>(C<sub>1</sub>) XOR IV

## Ejercicio 5.4
### **Keeping the IV secret in OFB mode does not make an exhaustive key search more complex.**
 1. Describe how we can perform a brute-force attack with unknown IV.
 2. What are the requirements regarding plaintext and ciphertext?
 - Para los pares de texto sin formato/texto cifrado seleccionados, podemos obtener el flujo de claves que fueron cifrados mediante **XOR**.</br> Esto significa que sabemos qué entrada se le dio al código primitivo para todos los bloques excepto el primer bloque (porque el flujo de claves se convierte en el IV del siguiente bloque).</br> Por lo que podemos intentar forzar una clave para que genere un flujo de claves a partir de entradas conocidas. Esto equivale a forzar un número en modo **CBC**. </br>El IV se puede obtener descifrando el flujo de claves del primer bloque una vez que haya alcanzado un alto nivel de confianza de que su clave de fuerza bruta no es un falso positivo.

## Ejercicio 5.5
### **Describe how the OFB mode can be attacked if the IV is not different for each execution of the encryption operation.**

 - Suponiendo que la clave sigue siendo la misma, el cifrado con el mismo IV producirá exactamente el mismo flujo de claves que los intentos de cifrado anteriores.
 </br>Sin conocer el par texto sin formato/texto cifrado, no hay forma de utilizar esta información para un ataque criptográfico. Sin embargo, si elige texto sin formato para un determinado bloque de mármol en el mensaje m1, esto se puede aplicar XOR con el texto cifrado conocido para derivar el flujo de claves para ese bloque. 
 </br>El flujo de claves se puede utilizar para descifrar el bloque b′i en mensaje m2 (cifrado con el mismo IV y generando así el mismo flujo de claves).


## Ejercicio 5.6
### **Propose an OFB mode scheme which encrypts one byte of plaintext at a time, e.g., for encrypting key strokes from a remote keyboard. The block cipher used is AES. 
Perform one block cipher operation for every new plaintext byte. Draw a block
diagram of your scheme and pay particular attention to the bit lengths used in your
diagram (cf. the descripton of a byte mode at the end of Sect. 5.1.4).

```
            +------------------------+
            |                        |
            |                        v
 Plaintext Byte ---->[XOR]----> Ciphertext Byte
               ^        |
               |        |
               |  +----------+
               |  | Extract  |
               |  | 1st Byte|
               |  +----------+
               |        |
               |        v
               |  +-------------+
               |  |   AES      |
               +--| Encryption |
                  |   (Key)    |
                  +-----^------+
                        |
                  128-bit IV
            (Updated for each byte)

```

## Ejercicio 5.7
### 5.7. As is so often true in cryptography, it is easy to weaken a seemingly strong scheme by small modifications. Assume a variant of the OFB mode by which we only feed back the 8 most significant bits of the cipher output. We use AES and fill the remaining 120 input bits to the cipher with 0s.146 5 More About Block Ciphers
1. Draw a block diagram of the scheme.

```
    +-----------------+
    | Byte de texto  |
    | claro (Plaintext)|
    +-----------------+
            |
            V
      +-----------+
      | AES Block |
      |   Cipher  |
      +-----------+
            |
            V
        +---+   (128 bits)
        | 8 | ------>
        |MSB| ---+
        +---+    |
                  |
                  V
                +-----------+
                |   Cifrado |
                |   CFB     |
                +-----------+
                  |
                  V
                +-----------+
                |   Cifrado |
                |   Texto   |
                |   Cifrado |
                +-----------+
```

2. Why is this scheme weak if we encrypt moderately large blocks of plaintext, say
100 kByte? What is the maximum number of known plaintexts an attacker needs
to completely break the scheme?

Esta variante es débil cuando se cifran bloques de texto más grandes (por ejemplo, 100 kBytes) porque solo
se están utilizando los 8 bits más significativos del cifrado de bloque AES, lo que limita la variabilidad 
en la secuencia cifrada. Esto facilita la predicción y el ataque, ya que los 120 bits restantes se llenan 
con ceros, lo que reduce la seguridad. El atacante necesita un número relativamente pequeño de textos claros 
conocidos para romper la clave.

3. Let the feedback byte be denoted by FB. Does the scheme become cryptograph-
ically stronger if we feedback the 128-bit value FB, FB, . . . , FB to the input (i.e.,
we copy the feedback byte 16 times and use it as AES input)?

La retroalimentación del valor de 128 bits en lugar de solo los 8 bits más significativos mejoraría la fortaleza 
del cifrado, ya que aumentaría la variabilidad en la secuencia cifrada. Esto haría que el esquema fuera más seguro 
y requeriría un número mucho mayor de textos claros conocidos para un ataque exitoso.

## Ejercicio 5.8
###  **In the text, a variant of the CFB mode is proposed which encrypts individual
bytes. Draw a block diagram for this mode when using AES as block cipher. Indicate
the width (in bit) of each line in your diagram.

```
[Plaintext (8 bits)]
        |
        V
      +---------------------+
      |      XOR Gate       |<----------+
      +---------------------+           |
              |                         |
              V                         |
[Ciphertext (8 bits)]                   |
              |                         |
              |                         |
      +---------------+                 |
      |               |                 |
      |   Shift       |                 |
      |  Register     |                 |
      | (120 bits)    |<----------------+
      |               | 
      +-------|-------+
              |
[IV or prev. AES output (128 bits)]
        |
        V
      +---------------------+
      |    AES Encryption   |
      +---------------------+
              |
              |------------------------+
              |                        |
[Most significant 8 bits]--------------+
```


## Ejercicio 5.9
### **We are using AES in counter mode for encrypting a hard disk with 1 TB of capacity.**</br>What is the maximum length of the IV?
- En AES-CTR (modo de contador), el IV (Vector de Inicialización) debe ser único para cada bloque de datos que se cifra. 

- La longitud del IV en AES-CTR generalmente es de 128 bits (16 bytes). Esta longitud es estándar y no depende del tamaño del disco duro. 

- Por lo tanto, en AES-CTR, el IV debe tener una longitud de 128 bits independientemente de la capacidad del disco duro. Pues el vector siempre seguirá el tamaño del bloque a cifrar

## Ejercicio 5.10
### **Verificar que la última parte sea una constante:**
  - En el estándar EMSA-PSS, la última parte de DB debe ser una secuencia constante de bits de acuerdo con las especificaciones del estándar. Esto se hace para garantizar que el relleno sea correcto. Verificar que esta constante esté presente en DB.

  - Aplicar la función de hash: </br>Utilizar una función de hash criptográfico, como SHA-256, para calcular el valor del hash del mensaje original (M'). El resultado será un valor hash fijo de longitud fija (Generalmente 32 bits).

  - H = Hash(M')

  Decodificar el valor EM: 
    El valor EM es la representación codificada de la firma. Se debe decodificar para obtener el valor entero correspondiente.

  - Desencriptar la firma: 
  Utilizar la clave pública del remitente para desencriptar el valor EM y obtener el valor de la firma original (S). La desencriptación se realiza utilizando el algoritmo RSA.

  - S = E^e mod N

  - Donde:
    - 'E' es el valor EM decodificado.
    - 'e' es el exponente público
    - 'N' es el módulo de la clave pública

  - Verificar la igualdad de hashes: Comparar el valor de hash calculado (H) con el valor de la firma desencriptada (S). Si son iguales, la firma es válida. Si no son iguales, la firma es inválida.

  - Si H == S, la firma es válida.
  - Si H ≠ S, la firma es inválida.

### **Finalizar la verificación:**
- El receptor debe informar el resultado de la verificación al remitente. Si la firma es válida, el mensaje se considera autenticado y no ha sido modificado en tránsito. Si la firma es inválida, el mensaje se considera sospechoso y no debe confiarse.

## Ejercicio 5.11
### Besides simple bit errors, the deletion or insertion of a bit yields even more
severe effects since the synchronization of blocks is disrupted. In most cases, the
decryption of subsequent blocks will be incorrect. A special case is the CFB mode
with a feedback width of 1 bit. Show that the synchronization is automatically re-
stored after κ + 1 steps, where κ is the block size of the block cipher.

En el modo CFB con un ancho de retroalimentación de 1 bit, la sincronización se restaura automáticamente 
después de κ + 1 pasos, donde κ es el tamaño del bloque del cifrador de bloques.

Esto se debe a que:

 - En el modo CFB, cada bloque de salida se combina mediante XOR con un bit del texto claro en cada paso.
 - Con un ancho de retroalimentación de 1 bit, el cifrado se procesa de un bit del texto cifrado a la vez.
 - Después de procesar κ bits (donde κ es el tamaño del bloque), el registro de desplazamiento de 
  retroalimentación se habrá llenado por completo con bits del texto cifrado.
 - El siguiente bit del texto claro se combina mediante XOR con el primer bit del texto cifrado en 
  el registro de desplazamiento.
 - Esto efectivamente desplaza hacia afuera el primer bit del texto cifrado y desplaza hacia adentro 
  el siguiente bit del texto cifrado, manteniendo la sincronización.
 - Por lo tanto, la sincronización se restaura después de κ + 1 pasos, donde κ es el tamaño del bloque del
  cifrador de bloques.


## Ejercicio 5.12

Búsqueda de clave pura sin uso de memoria:
 - Número de claves posibles: 2^56 para cada K1 y K2.
 - Número total de claves para buscar: 2^56 * 2^56 = 2^112.
 - Número de claves por segundo: 107.
 - Tiempo para buscar todo el espacio de claves: (2^112) / (107 claves/segundo) = 2^112 / 10^7 segundos.
 - Costo por circuito integrado (IC): $5.
 - Sobrecarga para construir la máquina: 50%.

Para calcular el costo, necesitamos considerar la cantidad de circuitos integrados requeridos:
 - Costo = (2^112 / 10^7 segundos) * $5 * (1 + 0.5) = 2^112 * $5 / 2 * 10^7 = $2^112 / 2 * 10^7.

Búsqueda de clave con el ataque meet-in-the-middle (tiempo-memoria):
 - Para este escenario, necesitamos almacenar las salidas intermedias en la búsqueda. Sin embargo,
  la cantidad de almacenamiento requerido y otros detalles no se proporcionan en la pregunta.
 - Costos por debajo de $1 millón con la Ley de Moore: 
 - La Ley de Moore predice que la capacidad de procesamiento de los circuitos integrados se duplicará
  aproximadamente cada dos años. Por lo tanto, los costos de la búsqueda de clave disminuirán a medida
  que pase el tiempo. Para determinar cuándo los costos caerán por debajo de $1 millón, se requeriría una
  estimación más precisa de los factores involucrados, como la velocidad de búsqueda y los costos de hardware.