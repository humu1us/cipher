from unittest import TestCase

from cipher import encrypt
from cipher import decrypt


class TestCipher(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.secrets = []
        cls.txt = "Hello, World!"
        cls.passwd = "secret_password"

    def test_encrypt(self):
        total = 100
        for i in range(total):
            self.secrets.append(encrypt(self.passwd, self.txt))

        for i in range(total):
            for j in range(i + 1, total):
                self.assertNotEqual(self.secrets[i], self.secrets[j])

    def test_decrypt(self):
        for s in self.secrets:
            self.assertEqual(decrypt(self.passwd, s), self.txt)

    def test_header(self):
        from cipher import cipher
        HEADER = cipher.HEADER
        cipher.HEADER = b"foo"

        secret = encrypt(self.passwd, self.txt)
        with self.assertRaises(Exception) as ctx:
            decrypt(self.passwd, secret)
        self.assertEqual(type(ctx.exception), RuntimeError)
        self.assertEqual(str(ctx.exception), "Missing header, cannot decrypt")

        cipher.HEADER = HEADER
        secret = encrypt(self.passwd, self.txt)
        self.assertEqual(decrypt(self.passwd, secret), self.txt)
