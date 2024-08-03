from Crypto.Cipher import ARC4, AES, DES, DES3, Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


class BlockCrypto:
    def __init__(self, cipher: str, mode: str):
        objects = {
            'AES128': {'obj': AES, 'key_size': 16},
            'AES192': {'obj': AES, 'key_size': 24},
            'AES256': {'obj': AES, 'key_size': 32},
            'DES': {'obj': DES, 'key_size': 8},
            '3DES': {'obj': DES3, 'key_size': 24},
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


class RC4:
    @staticmethod
    def encrypt(key: str, text: str) -> str:
        cipher = ARC4.new(key.encode())
        ciphertext = cipher.encrypt(text.encode())
        return b64encode(ciphertext).decode()

    @staticmethod
    def decrypt(key: str, crypted_text: str) -> str:
        ciphertext = b64decode(crypted_text.encode())
        cipher = ARC4.new(key.encode())
        return cipher.decrypt(ciphertext).decode()
