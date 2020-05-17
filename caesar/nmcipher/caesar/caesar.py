"""Encrypt and decrypt messages using Caesar cipher"""

class Caesar():
    """Class encrypts and decrypts messages using Caesar cipher"""

    @staticmethod
    def translate_symbols(key, symbols, reverse=False):
        """Helper method to create translation table for a given key and symbol set

        :param key: Encryption key
        :type key: int
        :param symbols: Encryption symbols
        :type symbols: string
        :param reverse: Create translation table for encryption or decrypttion (default is False)
        """
        table = {symbols[i]: symbols[(i + key) % len(symbols)] for i in range(len(symbols))}
        return str.maketrans(table if not reverse else {v: k for k, v in table.items()})

    def __init__(self, key, symbols):
        """Class initializer

        :param key: Encryption key
        :type key: int
        :param symbols: Encryption symbols that will be encrypted
        "type symbols: str
        """
        self._translation_table = self.translate_symbols(key, symbols)
        self._reverse_translation_table = self.translate_symbols(key, symbols, True)

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
