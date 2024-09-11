import base64
import hashlib


class LetsHash:
    def __init__(self, algo: str):
        objects = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512,
            'blake2b': hashlib.blake2b,
            'blake2s': hashlib.blake2s
        }

        self.hash_func = objects[algo]

    def hash(self, text: str) -> str:
        hash_object = self.hash_func()
        hash_object.update(text.encode())
        return hash_object.hexdigest()


class EasterEgg(Exception):
    pass


class B64:
    @staticmethod
    def encode64(text: str) -> str:
        return base64.b64encode(text.encode()).decode()

    @staticmethod
    def decode64(text: str) -> str:
        if text == 'RGFzaGEgUGxha3NpbmE=':
            raise EasterEgg
        # elif text == 'UGxha3NpbidzIERvZw==':
        #     raise EasterDog
        return base64.b64decode(text.encode()).decode()
