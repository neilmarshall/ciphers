"""Encrypt and decrypt messages using affine cipher"""

from math import gcd

class Affine():
    """Class encrypts and decrypts messages using affine cipher"""

    @staticmethod
    def find_modular_inverse(a, m):
        """Find modular inverse of a for modulus m"""
        if gcd(a, m) != 1:
            return None
        u_1, u_2, u_3 = 1, 0, a
        v_1, v_2, v_3 = 0, 1, m
        while v_3 != 0:
            q = u_3 // v_3
            v_1, v_2, v_3, u_1, u_2, u_3 = (u_1 - q * v_1), (u_2 - q * v_2), (u_3 - q * v_3), v_1, v_2, v_3
        return u_1 % m

    def __init__(self, key, symbols):
        """Class initializer

        :param key: Encryption key
        :type key: int
        :param symbols: Encryption symbols that will be encrypted
        "type symbols: str

        :example:
        >>> cipher = Affine(727, 'abcdefghijklmnopqrstuvwxyz')

        >>> cipher.encrypt('a secret message')
        'z rdbqds ldrrzfd'

        >>> cipher.decrypt('z rdbqds ldrrzfd')
        'a secret message'
        """
        key_a, key_b = key // len(symbols), key % len(symbols)
        if key_a == 1:
            raise ValueError("Key is weak when key A = 1")
        if key_b == 0:
            raise ValueError("Key is weak when key B = 0")
        if gcd(key_a, len(symbols)) != 1:
            raise ValueError(f"Multiplicative key ({key_a}) and length of symbols ({len(symbols)}) must be co-prime")

        self._translation_table = str.maketrans({symbols[i]: symbols[(i * key_a + key_b) % len(symbols)] for i in range(len(symbols))})

        self._reverse_translation_table = str.maketrans({symbols[i]: symbols[((i - key_b) * key_a) % len(symbols)] for i in range(len(symbols))})

    def encrypt(self, message):
        """Encrypt a message

        :param message: message to encrypt
        """
        return message.translate(self._translation_table)

    def decrypt(self, message):
        """Decrypt a message

        :param message: message to decrypt
        """
        return message.translate(self._reverse_translation_table)
