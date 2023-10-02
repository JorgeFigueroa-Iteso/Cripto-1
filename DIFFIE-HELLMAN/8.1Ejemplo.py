# EJERCICIO 8.1 del libro "Undestanding Cryptography"
from Crypto.Util.number import GCD

p = 29
g = 2

# ALICIA
a = 5

# BOB
b = 12

ka = pow(g, a, p)
kb = pow(g, b, p)

print(f'[+] ka: {ka}')
print(f'[+] kb: {kb}')

# ALICIA
kab = pow(kb, a, p)

# BOB
kba = pow(ka, b, p)

print(f'[+] kab: {kab}')
print(f'[+] kba: {kba}')