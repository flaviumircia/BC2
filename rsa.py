# RSA

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def calculate_n_fi(p, q):
    N = p * q
    FI = (p - 1) * (q - 1)
    return N, FI


def calculate_e_d(FI):
    e = 2
    while gcd(e, FI) != 1:
        e += 1
    d = mod_inverse(e, FI)
    return e, d


def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def encrypt(message, e, N):
    return mod_exp(message, e, N)


def decrypt(cryptogram, d, N):
    return mod_exp(cryptogram, d, N)


# Example usage
p = 7459  # Replace with your prime number
q = 7823  # Replace with your prime number

N, FI = calculate_n_fi(p, q)
e, d = calculate_e_d(FI)
print(e)
print(gcd(e, FI))

message = 7644254  # Replace with your message
cryptogram = encrypt(message, e, N)
decrypted_message = decrypt(cryptogram, d, N)

print("Original Message:", message)
print("Encrypted Message:", cryptogram)
print("Decrypted Message:", decrypted_message)
