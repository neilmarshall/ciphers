"""Encrypt and decrypt messages using simple substitution cipher"""

from string import ascii_letters

class Substitution():
    """Class encrypts and decrypts messages using simple substitution cipher"""

    def __init__(self, key):
        """Class initializer

        :param key: Encryption key; must be a permutation of the standard alphabet
        :type key: str

        :example:
        >>> cipher = Substitution('nopqrtuvwxijklmsyzabcdefgh')

        >>> cipher.encrypt('a secret message')
        'n arpzrb kraanur'

        >>> cipher.decrypt('n arpzrb kraanur')
        'a secret message'
        """
        if sorted(key.lower()) + sorted(key.upper()) != list(ascii_letters):
            raise ValueError("Invalid key - must be a (case-insensitive) permutation"
                             "of the entire alphabet")
        self.key = key.lower() + key.upper()
        self.translation_table = str.maketrans(ascii_letters, self.key)
        self.reverse_translation_table = str.maketrans(self.key, ascii_letters)

    def encrypt(self, message):
        """Encrypt a message

        :param message: message to encrypt
        """
        return message.translate(self.translation_table)

    def decrypt(self, message):
        """Decrypt a message

        :param message: message to decrypt
        """
        return message.translate(self.reverse_translation_table)
