#7.2. Computing modular exponentiation efficiently is inevitable for the practicabil-
#ity of RSA. Compute the following exponentiations xe mod m applying the square-
#and-multiply algorithm:
#1. x = 2, e = 79, m = 101
#2. x = 3, e = 197, m = 101
#After every iteration step, show the exponent of the intermediate result in binary
#notation.

def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
        print(f"Exponente en binario: {exponent} -> {bin(exponent)}")
    return result

# Caso 1
x1 = 2
e1 = 79
m1 = 101
resultado1 = modular_exponentiation(x1, e1, m1)
print(f"Resultado 1: {resultado1}")

# Caso 2
x2 = 3
e2 = 197
m2 = 101
resultado2 = modular_exponentiation(x2, e2, m2)
print(f"Resultado 2: {resultado2}")
