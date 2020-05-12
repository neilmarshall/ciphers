from string import ascii_letters

class Substitution():

    def __init__(self, key):
        if sorted(key.lower()) + sorted(key.upper()) != list(ascii_letters):
            raise ValueError("Invalid key - must be a (case-insensitive) permutation of the entire alphabet")
        self.key = key.lower() + key.upper()
        self.translation_table = str.maketrans(ascii_letters, self.key)
        self.reverse_translation_table = str.maketrans(self.key, ascii_letters)

    def encrypt(self, message):
        return message.translate(self.translation_table)

    def decrypt(self, message):
        return message.translate(self.reverse_translation_table)
