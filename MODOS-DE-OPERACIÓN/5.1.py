# 5.1. Consider the storage of data in encrypted form in a large database using AES.
# One record has a size of 16 bytes. Assume that the records are not related to one another. Which mode would be best suited and why?

# a: La modalidad de cifrado en cadena de bloques (CBC) no es apropiada ya que queremos poder acceder a registros individuales de forma aleatoria. Para este caso de uso muy simple, el modo de Libro de Códigos Electrónicos (ECB) probablemente sea el más apropiado, aunque podremos ver si dos registros son iguales. Esto podría solucionarse potencialmente utilizando algún tipo de sal si esto es un problema.

# 5.2. We consider known-plaintext attacks on block ciphers by means of an exhaustive key search where the key is k bits long. The block length counts n bits with n > k.

# 1. How many plaintexts and ciphertexts are needed to successfully break a block cipher running in ECB mode? How many steps are done in the worst case?
# - Depende del nivel de confianza con el que estés satisfecho. Dado que la longitud de la clave es menor en bits que la longitud del bloque, es posible (por el principio de las palomas en el agujero) que cada clave se mapee a un único texto cifrado. Sin embargo, no es seguro. Para un determinado texto plano, puede haber múltiples claves que se mapeen al mismo texto cifrado.

# 2. Assume that the initialization vector IV for running the considered block cipher in CBC mode is known. How many plaintexts and ciphertexts are now needed to break the cipher by performing an exhaustive key search? How many steps need now maximally be done? Briefly describe the attack.
# - Depende del nivel de confianza con el que estés satisfecho. Dado que la longitud de la clave es menor en bits que la longitud del bloque, es posible (por el principio de las palomas en el agujero) que cada clave se mapee a un único texto cifrado. Sin embargo, no es seguro. Para un determinado texto plano, puede haber múltiples claves que se mapeen al mismo texto cifrado.

# 3. How many plaintexts and ciphertexts are necessary, if you do not know the IV?
# - Depende del nivel de confianza con el que estés satisfecho. 
# Dado que la longitud de la clave es menor en bits que la longitud del bloque, es posible (por el principio del palomar) que cada clave se mapee a un único texto cifrado. 
# Sin embargo, no es seguro. Para un determinado texto plano, puede haber múltiples claves que se mapeen al mismo texto cifrado. Dependiendo de los valores reales de k y n, tener un segundo par (texto plano, texto cifrado) puede proporcionar un alto grado de certeza. Esto se debe a que es poco probable que la clave falsa también se mapee al mismo texto cifrado para otro texto plano. Para calcular la probabilidad de encontrar una clave falsa positiva (donde t es el número de textos planos elegidos que tienes), puedes usar esta fórmula:
# 2k-tn. 
# En el peor de los casos (que la última clave verificada de todas las posibles sea la correcta), tendrás que realizar 2k verificaciones.

# 4. Is breaking a block cipher in CBC mode by means of an exhaustive key search considerably more difficult than breaking an ECB mode block cipher?
# - Romper un cifrado en modo CBC no es tan costoso como romper un cifrado en modo ECB.
# Si el IV se conoce, romper un cifrado en modo CBC es equivalente a romper un cifrado en modo ECB.

