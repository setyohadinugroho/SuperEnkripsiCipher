from caesar import encrypt, decrypt
from transposisi import entrans, detrans

def senkripsi (p,kc,kt):
    return entrans(encrypt(p,kc),kt)

# print(senkripsi('akukaukua',3,3))


def sdekripsi (c,kc,kt):
    return detrans(decrypt(c,kc),kt)

# print(sdekripsi('dnnndxxxd',3,3))

