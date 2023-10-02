#8.12. Write a program which computes the discrete logarithm in Z∗p by exhaustive search. 
#The input parameters for your program are p, α , β . The program computes
#x where β = α x mod p.
#Compute the solution to log(106) 12375 in Z24691

from Crypto.Util.number import GCD
import math

def exhaustiveSearch(p, alpha, beta):
    for x in range(1, p):
        if pow(alpha, x, p) == beta:
            return x
    return None

#p = 24691
#alpha = 106
#beta = 12375

p = int(input(f'[+] Ingrese el valor de p: '))
alpha = int(input(f'[+] Ingrese el valor de alpha: '))
beta = int(input(f'[+] Ingrese el valor de beta: '))

print(f'[+] p: {p}')
print(f'[+] alpha: {alpha}')
print(f'[+] beta: {beta}')

x = exhaustiveSearch(p, alpha, beta)
print(f'[+] x: {x}')