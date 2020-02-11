import os
import shutil
from unittest import TestCase

from cipher import read
from cipher import write

HERE = os.path.abspath(os.path.dirname(__file__))


class TestCipher(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.secrets = []
        cls.txt = "Hello, World!"
        cls.passwd = "secret_password"
        cls.test_folder = "/tmp/cipher_test_folder"
        cls.encrypted_file = os.path.join(HERE, "resources", "example.secret")
        os.makedirs(cls.test_folder)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_folder)

    def test_read(self):
        self.assertEqual(read(self.encrypted_file, self.passwd), self.txt)

    def test_write(self):
        file = "encrypted.secret"
        file_path = os.path.join(self.test_folder, file)
        self.assertFalse(os.path.exists(file_path))

        write(file_path, self.passwd, self.txt)
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(read(file_path, self.passwd), self.txt)
