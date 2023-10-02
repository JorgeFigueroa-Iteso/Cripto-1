#Diffie-Hellman entre bob y alice

g = 2
exp = 467

#alice
a = 228
ka = pow(g, a, exp)

#bob
b = 57
kb = pow(g, b, exp)

print(f'[+] ka: {ka}')
print(f'[+] kb: {kb}')

#alice
kab = pow(kb, a, exp)

#bob
kba = pow(ka, b, exp)

print(f'[+] kab: {kab} == kba: {kba}')