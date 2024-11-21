class DES:
    # Implementasi metode DES seperti sebelumnya
    def ascii_to_bin(self, text):
        return ''.join(format(ord(c), '08b') for c in text)

    def bin_to_ascii(self, binary_str):
        chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        return ''.join(chr(int(char, 2)) for char in chars)

    def bin2hex(self, s):
        hex_str = ""
        for i in range(0, len(s), 4):
            hex_str += "{:X}".format(int(s[i:i+4], 2))
        return hex_str

    # Tambahkan metode lainnya untuk DES seperti generate_keys, encrypt, decrypt dll.