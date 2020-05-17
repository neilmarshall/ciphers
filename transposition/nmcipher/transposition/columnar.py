"""Encrypt and decrypt messages using transposition cipher"""

class Columnar():
    """Class encrypts and decrypts messages using transposition cipher"""

    @staticmethod
    def pad(string, length, padding=' '):
        """Add whitespace to the end of a string

        :param string: string to pad
        :type string: str
        :param length: length of padding to add
        :type length: int
        :param padding: character to pad string with (default is ' ')
        :type padding: str

        :example:
        >>> cipher = Columnar(4)

        >>> cipher.encrypt('a secret message')
        'ac s rmaseegetse'

        >>> cipher.decrypt('ac s rmaseegetse')
        'a secret message'
        """
        return string if len(string) >= length else Columnar.pad(string + padding, length, padding)

    @staticmethod
    def core_algorithm(key, message):
        """Core encryption algorithm

        :param key: Encryption key
        :type key: int
        """
        columns = tuple(Columnar.pad(message[i : i + key], key)
                        for i in range(0, len(message), key))
        return ''.join(''.join(column[i] for column in columns) for i in range(key))

    def __init__(self, key):
        """Class initializer

        :param key: Encryption key
        :type key: int
        """
        self.key = key

    def encrypt(self, message):
        """Encrypt a message

        :param message: message to encrypt
        """
        return Columnar.core_algorithm(self.key, message)

    def decrypt(self, message):
        """Decrypt a message

        :param message: message to decrypt
        """
        denominator = self.key if self.key != 0 else len(message)
        return Columnar.core_algorithm(len(message) // denominator, message).strip()
