from cipher import cipher


def read(path, passwd):
    with open(path, mode="rt") as fd:
        data = fd.read()

    dec = cipher.decrypt(passwd, data)
    return dec


def write(path, passwd, data):
    enc = cipher.encrypt(passwd, data)

    with open(path, mode="wt") as fd:
        fd.write(enc)
