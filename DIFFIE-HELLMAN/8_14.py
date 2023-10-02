# Parámetros de ElGamal
p = 31
alpha = 3
beta = 18

# Texto cifrado de y2
y2 = 25
# Valor de kE
kE = 6

# Pasos para llegar al inverso
y1 = 17
y1_kE = pow(y1, kE, p)  # Calcula (y1^kE) mod p
y1_kE_inverse = pow(y1_kE, -1, p)  # Calculo el inverso modular del valor anterior

# Calcular x2 usando la fórmula de descifrado dec = y2 ^  inv mod p
x2 = (y2 * y1_kE_inverse) % p

#Debe dar 7
print("Mensaje descifrado de x2:", x2)
