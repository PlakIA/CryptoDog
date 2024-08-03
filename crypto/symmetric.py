from base64 import b64encode, b64decode

from Crypto.Cipher import AES, DES, Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class BlockCrypto:
    def __init__(self, cipher: str, mode: str):
        objects = {
            'AES128': {'obj': AES, 'key_size': 16},
            'AES192': {'obj': AES, 'key_size': 24},
            'AES256': {'obj': AES, 'key_size': 32},
            'DES': {'obj': DES, 'key_size': 8},
            'Blowfish': {'obj': Blowfish, 'key_size': 16}
        }

        self.algo = objects[cipher]['obj']
        self.key_size = objects[cipher]['key_size']
        self.mode = mode

    def encrypt(self, key: str, text: str) -> str:
        key = pad(key.encode(), self.key_size)[:self.key_size]
        plaintext = pad(text.encode(), self.algo.block_size)

        if self.mode == 'ECB':
            cipher = self.algo.new(key, self.algo.MODE_ECB)
            ciphertext = cipher.encrypt(plaintext)
        elif self.mode == 'CBC':
            iv = get_random_bytes(self.algo.block_size)
            cipher = self.algo.new(key, self.algo.MODE_CBC, iv)
            ciphertext = iv + cipher.encrypt(plaintext)

        return b64encode(ciphertext).decode()

    def decrypt(self, key: str, crypted_text: str) -> str:
        key = pad(key.encode(), self.key_size)[:self.key_size]
        ciphertext = b64decode(crypted_text.encode())

        if self.mode == 'ECB':
            cipher = self.algo.new(key, self.algo.MODE_ECB)
            plaintext = cipher.decrypt(ciphertext)
        elif self.mode == 'CBC':
            iv = ciphertext[:self.algo.block_size]
            cipher = self.algo.new(key, self.algo.MODE_CBC, iv)
            plaintext = cipher.decrypt(ciphertext[self.algo.block_size:])

        return unpad(plaintext, self.algo.block_size).decode()
