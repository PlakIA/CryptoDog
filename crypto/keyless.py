import base64
import hashlib


class LetsHash:
    def __init__(self, algo: str):
        objects = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512
        }

        self.hash_func = objects[algo]

    def hash(self, text: str) -> str:
        hash_object = self.hash_func()
        hash_object.update(text.encode())
        return hash_object.hexdigest()


class B64:
    @staticmethod
    def encode(text: str) -> str:
        return base64.b64encode(text.encode()).decode()

    @staticmethod
    def decode(text: str) -> str:
        if text == 'RGFzaGEgUGxha3NpbmE=':
            return 'Easter Egg'
        elif text == 'UGxha3NpbidzIERvZw==':
            return 'Easter Dog'
        try:
            return base64.b64decode(text.encode()).decode()
        except Exception:
            return 'Decoding error'
