# Sección 10.1

## Autenticación del remitente e integridad de los datos

### 10.1.3 Autenticación e integridad

- **¿Por qué la autenticación del remitente siempre implica integridad de los datos?**
  1. Porque para poder autenticarnos necesitamos estar seguros de que los datos no hayan sido modificados en el camino por algún MITM.
  2. Necesitamos saber que la identidad del remitente sea siempre la misma y no haya sido interceptada.

- **¿La integridad implica autenticación del remitente?**
  - No, la integridad no implica necesariamente autenticación. Con la integridad, solo verificamos que el mensaje no haya sido modificado en el camino, pero no verifica que este mensaje sea de la fuente original.

# Sección 10.2

## Aspectos básicos de servicios de seguridad

### Privacidad e Integridad

1. **¿La privacidad garantiza siempre la integridad?**
   - No necesariamente. La privacidad garantiza que solo las personas autorizadas tengan acceso al dato, pero no garantiza que quien tenga acceso no pueda corromper esos datos.

2. **¿En qué orden se deben garantizar la confidencialidad y la integridad?**
   - Primero, la integridad y, después, la confidencialidad. Si primero encriptamos y luego verificamos la integridad, el hash sería sobre el mensaje cifrado. De la otra forma, estamos verificando la integridad del mensaje original y no del mensaje cifrado.

# Sección 10.3

## Diseño de un servicio de seguridad

![Imagen](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/FIRMAS-DIGITALES/aa.jpg)

Objetivo: Proveer integridad, confidencialidad y no repudio usando criptografía de clave pública en una comunicación de dos partes sobre un canal inseguro.

1. **Confidencialidad**
   a. Permitir solo al receptor acceder a la información.
   b. Usar criptografía asimétrica combinada con AES.
   c. Intercambiar la clave a través de Diffie-Hellman y cifrar con AES.

2. **Integridad**
   a. Detectar cualquier cambio en el mensaje durante su envío.
   b. Implementar firmas digitales en el mensaje.
   c. El emisor firma el mensaje y el receptor verifica la firma tras desencriptar con AES.

3. **No repudio**
   a. Asegurarse de que la autenticidad del mensaje no puede ser negada.
   b. Usar firmas digitales y timestamps.
   c. Enviar el mensaje con un timestamp y verificar con la llave privada del emisor.

# Sección 10.4

## Idea de negocio de un pintor

Requisitos: Transmisión segura de fotos y garantizar la autenticidad de las órdenes.

1. **Servicios de seguridad para la transmisión de fotos**
   - Confidencialidad
   - Autenticación
   - Integridad
   - No repudio
   - Control de acceso

2. **Elementos criptográficos**
   - Encriptación asimétrica para el intercambio de claves.
   - Encriptación simétrica para el cifrado de fotos.
   - Firmas digitales para la verificación.
   - Hashing para la integridad.
   - TLS para la combinación simétrica y asimétrica.
   - PKI para certificación.

# Sección 10.5

## Verificación de firmas RSA

Dado el esquema de firma RSA con clave pública (n = 9797, e = 131):

1. (x = 123, sig(x) = 6292) - **VÁLIDO**
2. (x = 4333, sig(x) = 4768) - **INVÁLIDO**
3. (x = 4333, sig(x) = 1424) - **VÁLIDO**

# Sección 10.6 Falsificación Existencial en RSA

Dado un esquema de firma RSA con la clave pública \( (n = 9797, e = 131) \), este documento demuestra cómo Oscar podría realizar un ataque de falsificación existencial, proporcionando un ejemplo con estos parámetros del esquema de firma digital RSA.

## Contexto

El receptor ha recibido \( (n, e) \) y puede usarlos para verificar el mensaje. Sin embargo, también podemos usarlos para que el receptor verifique nuestro mensaje falso.

## Proceso de Ataque

1. **Seleccionar una firma s arbitraria:**
   Oscar toma una \( s \) arbitraria en el rango de {0,1,2,…,9796}.
   
2. **Calcular \( x \):**
   Con la firma \( s \) seleccionada, Oscar calcula una \( x \) utilizando la ecuación: 
   x≡2^131 mod 9797
   x≡1347


## Verificación del Receptor

Cuando el receptor realiza la verificación de la firma, puede obtener los datos y pensar que son verídicos.
   x≡2^131 mod 9797
   x≡1347

## Conclusion

Este ejemplo demuestra cómo, bajo ciertas circunstancias, un atacante podría potencialmente manipular un esquema de firma RSA para hacer que un receptor crea que un mensaje falso es verídico.

# 10.7 Ataque de Intermediario en un Esquema de Firma Digital RSA

![Imagen](https://github.com/JorgeFigueroa-Iteso/Cripto-1/blob/main/FIRMAS-DIGITALES/sd.jpg)

En un esquema de firma digital RSA, Bob firma mensajes \(x_i\) y los envía junto con las firmas \(s_i\) y su clave pública a Alice. La clave pública de Bob es el par \((n, e)\), y su clave privada es \(d\).

El objetivo de Oscar es realizar un ataque de intermediario, es decir, reemplazar la clave pública de Bob por la suya en el canal de comunicación. Su meta es alterar mensajes y proporcionarlos con una firma digital que se verifique correctamente en el lado de Alice. A continuación, se describen los pasos que Oscar debe seguir para llevar a cabo un ataque exitoso:

## Pasos para el Ataque de Intermediario

1. **Interceptar el mensaje:** Oscar debe de alguna manera obtener acceso al mensaje que originalmente estaba destinado a Bob.

2. **Firmar el mensaje con su propia clave privada:** Una vez que Oscar tiene el mensaje, debe firmarlo con su propia clave privada para generar una nueva firma \(s'\). Ahora, el mensaje tiene una firma falsa.

3. **Reemplazar la clave pública de Bob:** Oscar reemplaza la clave pública de Bob, que originalmente era \((n, e)\), por su propia clave pública \((n', e')\). Esto se hace en el canal de comunicación, de manera que cuando Alice reciba los datos, creerá que provienen de Bob.

4. **Enviar el mensaje, firma y clave pública falsos a Alice:** Oscar envía el mensaje modificado, la nueva firma \(s'\), y su propia clave pública \((n', e')\) a Alice. Desde la perspectiva de Alice, todo parece correcto ya que los datos llevan la firma de Bob y se verifican correctamente con la clave pública de Oscar.

## Consecuencias del Ataque

Este tipo de ataque de intermediario puede tener graves consecuencias, ya que Alice podría creer que está comunicándose con Bob cuando en realidad está interactuando con Oscar. Esto podría llevar a la manipulación de mensajes y la difusión de información falsa.

Para prevenir este tipo de ataques, es fundamental implementar medidas de seguridad, como el uso de canales seguros de comunicación y la verificación adecuada de las claves públicas de los comunicantes. Además, es importante proteger las claves privadas para que no caigan en manos equivocadas.
