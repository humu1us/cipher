import os
import base64
from Crypto.Cipher import AES
import cipher.core.pkcs7 as pkcs7
from cipher.core.derivation import derive_password

HEADER = b"_humu1us_enc__"


def check_header(raw):
    return raw[:14] == HEADER


def encrypt(passwd, text):
    padded = pkcs7.pad(text)
    salt = os.urandom(8)
    key, iv = derive_password(passwd, salt)
    c = AES.new(key, AES.MODE_CBC, iv)
    encrypted = base64.b64encode(HEADER + salt + c.encrypt(padded))

    return base64.b64encode(encrypted).decode("utf-8")


def decrypt(passwd, encrypted):
    raw = base64.b64decode(base64.b64decode(encrypted))
    if not check_header(raw):
        raise RuntimeError("Missing header, cannot decrypt")

    salt = raw[14:22]
    key, iv = derive_password(passwd, salt)
    encrypted = raw[22:]

    c = AES.new(key, AES.MODE_CBC, iv)
    text = pkcs7.unpad(c.decrypt(encrypted))

    return text.decode("utf-8")
