import numpy as np
#4.10. In the following, we check the diffusion properties of AES after a single 
#round. Let W = (w0 , w1 , w2 , w3 ) = (0x01000000, 0x00000000, 0x00000000,
#0x00000000) be the input in 32-bit chunks to a 128-bit AES. The subkeys for the
#computation of the result of the first round of AES are W0 , . . . ,W7 with 32 bits each
#are given by
#W0 = (0x2B7E1516),
#W1 = (0x28AED2A6),
#W2 = (0xABF71588),
#W3 = (0x09CF4F3C),
#W4 = (0xA0FAFE17),
#W5 = (0x88542CB1),
#W6 = (0x23A33939),
#W7 = (0x2A6C7605).
#Use this book to figure out how the input is processed in the first round (e.g., S-
#Boxes). For the solution, you might also want to write a short computer program or
#use an existing one. In any case, indicate all intermediate steps for the computation
#of ShiftRows, SubBytes and MixColumns!
#1. Compute the output of the first round of AES to the input W and the subkeys
#W0 , . . . ,W7.

#Para recordar, AES opera en bloques de 128 bits y utiliza varias rondas para encriptar 
#los datos. Cada ronda tiene varios pasos:
#SubBytes: Cada byte del estado es reemplazado por otro byte según una tabla de sustitución (S-Box).
#ShiftRows: Los bytes de cada fila del estado se desplazan circularmente un cierto número de posiciones.
#MixColumns: Cada columna del estado se multiplica por una matriz fija.
#AddRoundKey: Cada byte del estado se combina con un byte de la subclave de la ronda.

#El codigo quedaria algo así, siguiendo estos pasos:

# Tabla SBox utilizada en la operación SubBytes
s_box = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

# Matriz de mezcla utilizada en la operación MixColumns
mix_matrix = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

# Función para realizar la operación SubBytes
def sub_bytes(state):
    new_state = bytearray()  # Usar bytearray para trabajar con bytes en lugar de enteros
    for byte in state:
        new_state.append(s_box[byte])  # Reemplaza cada byte utilizando s_box
    return new_state

# Función para realizar la operación ShiftRows
def shift_rows(state):
    state = np.array(state).reshape((4, 4))
    for i in range(4):
        row = list(state[i])  # Convertir el byte a una lista de un solo elemento
        state[i] = row[i:] + row[:i]  # Realizar la operación de rebanado en la lista
    return state.flatten().tolist()

# Función para realizar la operación MixColumns
def mix_columns(state):
    state = np.array(state).reshape((4, 4))
    new_state = np.zeros((4, 4), dtype=np.uint8)
    for col in range(4):
        for row in range(4):
            new_state[row][col] = (
                mul(0x02, state[row][col])
                ^ mul(0x03, state[(row + 1) % 4][col])
                ^ state[(row + 2) % 4][col]
                ^ state[(row + 3) % 4][col]
            )
    return new_state.flatten().tolist()
# Función para realizar la operación AddRoundKey
def add_round_key(state, round_key):
    new_state = []
    for i in range(len(state)):
        new_state.append(state[i] ^ round_key[i])  # Operación XOR entre el estado y la clave de ronda
    return new_state

# Función para multiplicación en el campo Galois (GF(2^8))
def mul(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p

# Define tu entrada y tus subclaves aquí
input_state = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
round_key = [0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C]

# Realiza las operaciones de una ronda AES
state = sub_bytes(input_state)
state = shift_rows(state)
state = mix_columns(state)
state = add_round_key(state, round_key)

# Muestra el estado después de una ronda AES
print("Primera ronda de AES: ",state)

####################################################################################################################################3

#2. Compute the output of the first round of AES for the case that all input bits are
#zero.
#Si todos los bits de entrada son cero, después de SubBytes y ShiftRow todos los bits seguirán siendo cero.
#La operación MixColumns tampoco cambiará esto, ya que está multiplicando por cero. Finalmente, el AddRoundKey 
#simplemente hará un XOR de los bits de la subclave de ronda con cero, así que el
#resultado de la primera ronda será simplemente la subclave de ronda.


#3. How many output bits have changed? Remark that we only consider a single
#round — after every further round, more output bits will be affected (avalanche
#effect).
#Para entender cuántos bits de salida han cambiado, simplemente necesitamos comparar el resultado de la primera
#ronda con el bloque de entrada, bit a bit. Esto nos permite observar el efecto avalancha, incluso después de
#una sola ronda, y cómo cada bit de entrada afecta potencialmente a muchos bits de salida.
