# El-Gamal

import random
from sympy import mod_inverse

# Constants
P = 1640369973901140749156079796758685131616742442308270026953773
G = 4184
PRIVATE_KEY = 191

def generate_random_k(p):
    # Generate a random k within the range [1, p - 1]
    return random.randint(1, p - 1)

def compute_public_key(g, private_key, p):
    # Calculate public key: Y = (G ^ X) mod P
    return pow(g, private_key, p)

def encrypt_message(p, g, private_key, pub_key, message):
    k = generate_random_k(p)
    c1 = pow(g, k, p)  # Ciphertext part 1
    unique_key = pow(pub_key, k, p)
    c2 = (unique_key * message) % p  # Ciphertext part 2
    return c1, c2

def encrypt_messages(p, g, private_key, pub_key, messages):
    encrypted_messages = []
    for message in messages:
        c1, c2 = encrypt_message(p, g, private_key, pub_key, message)
        encrypted_messages.append((c1, c2))
    return encrypted_messages

def decrypt_messages(p, private_key, encrypted_messages):
    decrypted_messages = []
    for c1, c2 in encrypted_messages:
        unique_k = pow(c1, private_key, p)
        inv_unique_k = mod_inverse(unique_k, p)
        decrypted_message = (c2 * inv_unique_k) % p
        decrypted_messages.append(decrypted_message)
    return decrypted_messages

# Compute public key
pub_key = compute_public_key(G, PRIVATE_KEY, P)
print("P =", P, ", G =", G)
print("Private Key:", PRIVATE_KEY)
print("Public Key:", pub_key)

# Encrypt and decrypt messages
messages = [12374661241314321237466124131432, 45614761443124324561476144312432, 78955361343217895536134321325421, 58913541554321001354155432341252, 27811441244322781144124432278114]  # Example messages to encrypt
encrypted_messages = encrypt_messages(P, G, PRIVATE_KEY, pub_key, messages)
print("Encrypted Messages:")
for c1, c2 in encrypted_messages:
    print("({}, {})".format(c1, c2))

decrypted_messages = decrypt_messages(P, PRIVATE_KEY, encrypted_messages)
print("Decrypted Messages:", decrypted_messages)