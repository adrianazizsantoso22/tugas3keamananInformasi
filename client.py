import socket
from desAlgo import DES
from rsaAlgo import RSA

def main():
    des_algo = DES()
    rsa_algo = RSA()

    # Generate RSA keys
    p, q = 61, 53  # Example primes
    public_key, private_key = rsa_algo.generate_keypair(p, q)

    # Setup socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 1234))

    # Send encrypted DES key
    des_key = "AMANAJAA"  # Example DES Key
    encrypted_key = rsa_algo.encrypt(des_key, public_key)
    client.send(encrypted_key.to_bytes((encrypted_key.bit_length() + 7) // 8, 'big'))

    while True:
        msg = input("A: ")
        if msg.lower() == 'quit':
            client.send(b'quit')
            break

        client.send(msg.encode("utf-8"))
        cipher_text = client.recv(1024).decode("utf-8")
        print(f"Cipher Text (Hex): {cipher_text}")

    client.close()

if __name__ == "__main__":
    main()