# Diffie-Hellman

import random
import sympy

p_bits = input("Enter number of bits of prime number: ")
p_bits = int(p_bits)

p_bitsmax = ((2 ** p_bits) - 1)
p_bitsmin = (2 ** (p_bits - 1))

p = sympy.randprime(p_bitsmin, p_bitsmax)

g = random.randint(1, p-1)
a = random.randint(1, p-1)
b = random.randint(1, p-1)

A = pow(g, a, p)
B = pow(g, b, p)
k1 = pow(B, a, p)
k2 = pow(A, b, p)

print("The value of p selected:", p)
print("The value of g selected:", g)
print("The value of a selected by Alice:", a)
print("The value of b selected by Bob:", b)
print("The value of A sent to Bob by Alice:", A)
print("The value of B sent to Alice by Bob:", B)
print("The value of shared key computed by Alice:", k1)
print("The value of shared key computed by Bob:", k2)
print("")

if k1 == k2:
    print("The shared keys match.")
else:
    print("The shared keys don't match. Something went wrong.")