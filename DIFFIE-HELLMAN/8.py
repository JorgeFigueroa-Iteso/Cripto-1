#Let’s start with an easy one. Determine the order of all elements of the multi-
#plicative groups of:
#1. Z∗5
#2. Z∗7
#3. Z∗13

# EJERCICIO 8 del libro "Undestanding Cryptography"
from Crypto.Util.number import GCD

def generateOrd(mod):

    x=[]
    for num in range(1, mod):
        x.append(num)
    print(f'\nRango manejado: {x}', end='')

    matrix=[[(i*j)%mod for j in range (mod)] for i in range(mod)]
    #Mostrar la matriz sin el 0
    print("\nMatriz: ")
    for i in range(mod):
        for j in range(mod):
            if matrix[i][j]!=0:
                print(matrix[i][j],end=" ")
            else:
                print("",end="")
        print()

    #Mostrar la diagonal de la matriz
    print("Diagonal: ",end="")
    for i in range(mod):
        if matrix[i][i]!=0:
            print(matrix[i][i],end=" ")
        else:
            print("",end="")
    print(f'\nGenerador de {mod}: {find_primitive_roots(mod)}')


def is_primitive_root(g, p):
    order = 1
    while pow(g, order, p) != 1:
        order += 1
    return order == (p - 1)

def find_primitive_roots(p):
    primitive_roots = []
    for g in range(2, p):
        if is_primitive_root(g, p):
            primitive_roots.append(g)
    return primitive_roots

print(f'\n[+] Generators:')
z4969=find_primitive_roots(4969)
print(f'[+] z4969: {len(z4969)}')

#Determine the smallest generator a ∈ Z∗4969 with a > 1000.
print(f'\n[+] Determine the smallest generator a ∈ Z∗4969 with a > 1000.')
print(f'[+] z4969: {z4969[0]}')

## What measures can be taken in order to simplify the search for generators for arbitrary groups Z∗p?
# a: Se puede hacer una lista de los generadores de los grupos y buscar en esa lista
