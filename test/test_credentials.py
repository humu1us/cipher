import os
from unittest import TestCase

from cipher import Credentials

HERE = os.path.abspath(os.path.dirname(__file__))


class TestCredentials(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.passwd = "secret_password"
        cls.encrypted = os.path.join(HERE, "resources", "credentials.secret")

    def test_file_not_found(self):
        with self.assertRaises(Exception) as ctx:
            Credentials("wrong_path", self.passwd)
        self.assertEqual(type(ctx.exception), FileNotFoundError)
        expected = "[Errno 2] No such file or directory: 'wrong_path'"
        self.assertEqual(str(ctx.exception), expected)

    def test_wrong_passwd(self):
        with self.assertRaises(Exception) as ctx:
            Credentials(self.encrypted, "wrong_passwd")
        self.assertEqual(type(ctx.exception), RuntimeError)
        self.assertEqual(str(ctx.exception), "Cannot load config")

    def test_decrypt(self):
        expected = {
            "token": "some_token_app",
            "dsn": "engine://user:pass@host:port/name",
        }
        cred = Credentials(self.encrypted, self.passwd)
        self.assertEqual(cred.token, expected["token"])
        self.assertEqual(cred.dsn, expected["dsn"])
