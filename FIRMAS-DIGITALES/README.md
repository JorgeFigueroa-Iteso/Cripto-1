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
