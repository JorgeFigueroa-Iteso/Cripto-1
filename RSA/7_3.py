#7.3. Encrypt and decrypt by means of the RSA algorithm with the following system
#parameters:
#1. p = 3, q = 11, d = 7, x = 5
#2. p = 5, q = 11, e = 3, x = 9
#Only use a pocket calculator at this stage.

p1 = 3
q1 = 11
d1 = 7
x1 = 5

N1 = p1 * q1
phi_N1 = (p1 - 1) * (q1 - 1)

e1 = pow(d1, -1, phi_N1)
print(f"\nExponente e calculado -> {e1}")

encrypt1 = pow(x1, e1, N1)
print(f"Mensaje encriptado (Caso 1): ", encrypt1)

decrypt1 = pow(encrypt1, d1, N1)
print(f"Mensaje desencriptado -> {x1} (Caso 1): ", decrypt1)

print("\n")

p2 = 5
q2 = 11
e2 = 3
x2 = 9

N2= p2 * q2
phi_N2 = (p2 - 1) * (q2 - 1)

key=pow(e2, -1, phi_N2)
print(f"Clave d calculada -> {key}")

encrypt2 = pow(x2, e2, N2)
print("Mensaje encriptado (Caso 2): ",encrypt2)

decrypt2=pow(encrypt2, key, N2)
print(f"Mensaje desencriptado -> {x2} (Caso 2): ",decrypt2)
