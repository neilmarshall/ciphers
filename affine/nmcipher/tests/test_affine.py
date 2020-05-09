import unittest

from affine import Affine

class TestAffine(unittest.TestCase):
    def setUp(self):
        key = 2894
        self.message = '"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing'
        self.encrypted_message = '"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu'
        self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
        self.cipher = Affine(key, self.symbols)

    def test_encryption(self):
        self.assertEqual(self.cipher.encrypt(self.message), self.encrypted_message)

    def test_decryption(self):
        self.assertEqual(self.cipher.decrypt(self.encrypted_message), self.message)

    def test_weak_value_for_keyA_raises_error(self):
        key = 67
        self.assertRaisesRegex(ValueError, '^Key is weak when key A = 1$', Affine, key, self.symbols)

    def test_weak_value_for_keyB_raises_error(self):
        key = 198
        self.assertRaisesRegex(ValueError, '^Key is weak when key B = 0$', Affine, key, self.symbols)

    def test_coprime_keys_raises_error(self):
        key = 167
        self.assertRaisesRegex(ValueError, r'Multiplicative key \(2\) and length of symbols \(66\) must be co-prime', Affine, key, self.symbols)
