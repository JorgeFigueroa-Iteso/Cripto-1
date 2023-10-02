# Parámetros de ElGamal (Prueba con los mismos parametros del ej. 14)
p = 31
alpha = 3
beta = 18

# Datos conocidos
j = 2  # Se lo puse paea indicar que el rango de j es (1 <= j <= n-1)
y_j = 25
i_j = 17

# Calcular xj:
# 1. calcula beta^(-i_j) mod p
beta_inverse_ij = pow(beta, -i_j, p)
# 2. sacar xj con la formula xj = yj * int beta (ij) mod p (La formula de Kelchoff)
x_j = (y_j * beta_inverse_ij) % p

print(f"El mensaje x{j} es: {x_j}")

