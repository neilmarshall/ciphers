import unittest

from columnar import Columnar

class TestColumn(unittest.TestCase):
    def test_encryption(self):
        keys = (8, 9)
        messages = (
            "Common sense is not so common.",
            "Underneath a huge oak tree there was of swine a huge company,"
        )
        encrypted_messages = (
            "Cenoonommstmme oo snnio. s  s c ",
            "Uhot  on ahoamdakef pe  r harhtesunnur wgyegewie,aeean  t  sec "
        )
        for key, message, encrypted_message in (zip(keys, messages, encrypted_messages)):
            with self.subTest(key=key, message=message, encrypted_message=encrypted_message):
                cipher = Columnar(key)
                self.assertEqual(cipher.encrypt(message), encrypted_message)

    def test_decryption(self):
        keys = (8, 9)
        messages = (
            "Cenoonommstmme oo snnio. s  s c ",
            "Uhot  on ahoamdakef pe  r harhtesunnur wgyegewie,aeean  t  sec "
        )
        decrypted_messages = (
            "Common sense is not so common.",
            "Underneath a huge oak tree there was of swine a huge company,"
        )
        for key, message, decrypted_message in (zip(keys, messages, decrypted_messages)):
            with self.subTest(key=key, message=message, decrypted_message=decrypted_message):
                cipher = Columnar(key)
                self.assertEqual(cipher.decrypt(message), decrypted_message)
