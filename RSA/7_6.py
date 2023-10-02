#7.6. Verify the RSA with CRT example in the chapter by computing yd = 15103 mod
#143 using the square-and-multiply algorithm.

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
y = 15
e = 103
m = 143
resultado1 = modular_exponentiation(y, e, m)
print(f"Resultado : {resultado1}")

