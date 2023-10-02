# Sección 5

## Ejercicio 5.1
- **Consider the storage of data in encrypted form in a large database using AES.**
 1. One record has a size of 16 bytes. Assume that the records are not related to one another. Which mode would be best suited and why?
 2. La modalidad de cifrado en cadena de bloques (CBC) no es apropiada ya que queremos poder acceder a registros individuales de forma aleatoria. Para este caso de uso muy simple, el modo de Libro de Códigos Electrónicos (ECB) probablemente sea el más apropiado, aunque podremos ver si dos registros son iguales. Esto podría solucionarse potencialmente utilizando algún tipo de sal si esto es un problema.

## Ejercicio 5.2
- **We consider known-plaintext attacks on block ciphers by means of an exhaustive key search where the key is k bits long. The block length counts n bits with n > k.**
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
- **In a company, all files which are sent on the network are automatically encrypted by using AES-128 in CBC mode. A fixed key is used, and the IV is changed once per day. The network encryption is file-based, so that the IV is used at the beginning of every file.**
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
- **Keeping the IV secret in OFB mode does not make an exhaustive key search more complex.**
 1. Describe how we can perform a brute-force attack with unknown IV.
 2. What are the requirements regarding plaintext and ciphertext?

