import random
from sympy import isprime, mod_inverse

class RSA:
    def generate_keypair(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537  # Common choice for e
        d = mod_inverse(e, phi)
        return ((e, n), (d, n))  # Public and private key

    def encrypt(self, plaintext, public_key):
        e, n = public_key
        plaintext = int.from_bytes(plaintext.encode('utf-8'), 'big')
        cipher = pow(plaintext, e, n)
        return cipher

    def decrypt(self, ciphertext, private_key):
        d, n = private_key
        plaintext = pow(ciphertext, d, n)
        return plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big').decode('utf-8')