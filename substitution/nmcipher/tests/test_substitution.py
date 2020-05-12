import unittest

from substitution import Substitution

class TestSubstitution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
        cls.decrypted_message = ('If a man is offered a fact which goes against '
            'his instincts, he will scrutinize it closely, and unless the evidence '
            'is overwhelming, he will refuse to believe it. If, on the other hand, '
            'he is offered something which affords a reason for acting in accordance '
            'to his instincts, he will accept it even on the slightest evidence. The '
            'origin of myths is explained in this way. -Bertrand Russell')
        cls.encrypted_message = ('Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj '
            'isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa '
            'sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, '
            'ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa '
            'jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia '
            'pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm')

    def test_encryption(self):
        cipher = Substitution(self.key)
        self.assertEqual(cipher.encrypt(self.decrypted_message), self.encrypted_message)

    def test_decryption(self):
        cipher = Substitution(self.key)
        self.assertEqual(cipher.decrypt(self.encrypted_message), self.decrypted_message)

    def test_invalid_key_raises_error(self):
        self.assertRaises(ValueError, Substitution, "abcdef")
