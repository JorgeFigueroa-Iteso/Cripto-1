def MCD(a, b):
    if b == 0:
        return a, 1, 0
    else:
        mcd, u, v = MCD(b, a % b)
        return mcd, v, u - (a // b) * v

def modinv(a, m):
    mcd, u, _ = MCD(a, m)
    if mcd != 1:
        raise ValueError(f"{a} y {m} no son coprimos")
    else:
        return u % m

p = 31
q = 37
e = 17
y = 2

n = p * q
phi_n = (p - 1) * (q - 1)

# Calcular el inverso multiplicativo de e modulo phi_n para obtener d
_, d, _ = MCD(e, phi_n)
if d < 0:
    d += phi_n

# Calcular dp, dq, y qinv
dp = d % (p - 1)
dq = d % (q - 1)
qinv = modinv(q, p)

# Aplicar el Teorema Chino del Resto
mp = pow(y, dp, p)
mq = pow(y, dq, q)
h = (qinv * (mp - mq)) % p
m = mq + h * q

# Descifrado sin CRT
no_crt = pow(y, d, n)

print("Resultado usando CRT:", m)
print("Resultado sin CRT:", no_crt)
