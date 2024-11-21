from desAlgo import DES
from rsaAlgo import RSA

def main():
    des_algo = DES()
    rsa_algo = RSA()

    # Example plaintext and keys
    pt = "ADNAN ABDULLAH JUAN | 5025221155"
    key = "AMANAJAA"

    # Test DES
    pt_bin = des_algo.ascii_to_bin(pt)
    key_bin = des_algo.ascii_to_bin(key)
    rkb, rk = des_algo.generate_keys(key_bin)

    print("Encryption")
    cipher_text = des_algo.encrypt(pt_bin, rkb, rk)
    print(f"Cipher Text (Hex): {des_algo.bin2hex(cipher_text)}")

    print("Decryption")
    rkb_rev = rkb[::-1]
    rk_rev = rk[::-1]
    decrypted_text = des_algo.decrypt(cipher_text, rkb_rev, rk_rev)
    print(f"Decrypted Text: {des_algo.bin_to_ascii(decrypted_text)}")

if __name__ == "__main__":
    main()