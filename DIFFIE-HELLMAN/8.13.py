# 8.13. Encrypt the following messages with the Elgamal scheme (p = 467 and α = 2):
#1. k pr = d = 105, i = 213, x = 33
#2. k pr = d = 105, i = 123, x = 33
#3. k pr = d = 300, i = 45, x = 248
#4. k pr = d = 300, i = 47, x = 248
#Now decrypt every ciphertext and show all steps.

from Crypto.Util.number import GCD

# Computar B: B = α^d mod p
# Encrypt: y = (B^k mod p, xB^k mod p)
# Decrypt: x = y2(y1^d)^-1 mod p

def encrypt(p, alpha, d, k, x):
    B = pow(alpha, d, p)
    y1 = pow(alpha, k, p)
    y2 = (x * pow(B, k, p)) % p
    return y1, y2

def decrypt(p, alpha, d, y1, y2):
    B = pow(alpha, d, p)
    x = (y2 * pow(y1, -d, p)) % p
    return x

def encryptAndDecrypt(d, k, x, p, alpha):
    for i in range(len(d)):
        dt = d[i]
        kt = k[i]
        xt = x[i]
        print(f'[+] {i+1}')
        y1, y2 = encrypt(p, alpha, dt, kt, xt)
        print(f'[+] y\'s: ({y1}, {y2})')
        xt = decrypt(p, alpha, dt, y1, y2)
        print(f'[+] x: {xt}')
        print()

p = 467
alpha = 2

# Encrypt and Decrypt
d = [105, 105, 300, 300]
k = [213, 123, 45, 47]
x = [33, 33, 248, 248]

encryptAndDecrypt(d, k, x, p, alpha)