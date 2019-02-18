from Crypto.Cipher.AES import block_size

AES_BLOCK_SZ = block_size


def pad(text):
    pad_len = AES_BLOCK_SZ - (len(text) % AES_BLOCK_SZ)
    return text + (chr(pad_len) * pad_len)


def unpad(text):
    pad_len = text[-1]
    return text[:-pad_len]
