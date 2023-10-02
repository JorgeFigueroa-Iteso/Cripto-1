# EJERCICIO 8.2 del libro "Undestanding Cryptography"
from Crypto.Util.number import GCD

#Mostrar tablas x mod y
n = int(input(f'[+] Ingrese el valor de n: '))
print(f'\nx mod {n}\n')

# Tabla de 1 a n-1
def TablaGeneradora(n):
    for i in range(n):
        # Imprime los headers
        print(f'{i} |', end='')
    print()
    print('-' * (n * 3))
    for i in range(1, n):
        print(f'{i} |', end='')
        for j in range(1, n):
            print(f'{(i * j) % n} |', end='')
        print()

TablaGeneradora(n)

# 8.2. We consider the group Z ∗ 53 . What are the possible element orders? How many elements exist for each order?
print(f'\n8.2. We consider the group Z ∗ 53 . What are the possible element orders? How many elements exist for each order?\n')
n = 53
print(f'[+] n: {n}')
print(f'[+] Elementos: {n - 1}')
print(f'[+] Ordenes: {n - 1}')