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
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 1234))
    server.listen(5)
    print("Server started, waiting for connections...")

    client, addr = server.accept()
    print(f"Connected to {addr}")

    try:
        while True:
            # Receive encrypted DES key
            encrypted_key = client.recv(1024)
            decrypted_key = rsa_algo.decrypt(int.from_bytes(encrypted_key, 'big'), private_key)
            print(f"Decrypted DES Key: {decrypted_key}")

            # Receive message
            msg = client.recv(1024).decode("utf-8")
            if msg.lower() == 'quit':
                break

            # Process message with DES
            msg_bin = des_algo.ascii_to_bin(msg)
            cipher_text = des_algo.encrypt(msg_bin, des_algo.generate_keys(decrypted_key))
            client.send(des_algo.bin2hex(cipher_text).encode("utf-8"))

    finally:
        client.close()
        server.close()
        print("Server closed.")

if __name__ == "__main__":
    main()