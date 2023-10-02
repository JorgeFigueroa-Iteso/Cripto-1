#7.1. Let the two primes p = 41 and q = 17 be given as set-up parameters for RSA.
#1. Which of the parameters e1 = 32, e2 = 49 is a valid RSA exponent? Justify your
#choice.
#2. Compute the corresponding private key Kpr = (p, q, d). Use the extended Eu-
#clidean algorithm for the inversion and point out every calculation step.

def MCD(a, b):
    if a == 0:
        return b, 0, 1
    mcd, U, V = MCD(b % a, a)
    u = V - (b // a) * U
    v = U
    return mcd, u, v
p = 41
q = 17
e=int(input("e: "))
N=p*q
Nt=(p-1)*(q-1)
print(f"N={N}\nNt={Nt}")
mcd, u, v = MCD(Nt, e)
if mcd==1:
  print(f"[+] Los numeros {Nt} y {e} son primos relativos\n\t- mcd -> {mcd}\n\t- Inverso de {Nt} -> {u}\n\t- Inverso de {e} -> {v}")

k=v
print(f"Key={k}")
