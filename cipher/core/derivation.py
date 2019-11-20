from hashlib import md5
from Crypto.Cipher import AES

KEY_LEN = max(AES.key_size)


def derive_password(passwd, salt):
    pwd = passwd.strip()
    max_len = KEY_LEN + AES.block_size
    # Add salt to passwd
    pwd = pwd.encode("ascii", "ignore") + salt

    md5_digest = md5(pwd).digest()

    d = md5_digest + pwd
    for i in range(1, max_len):
        d = md5(d).digest()
        md5_digest += d
        d += pwd

    return md5_digest[:KEY_LEN], md5_digest[KEY_LEN:max_len]
