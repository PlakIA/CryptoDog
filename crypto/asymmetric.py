import os

import gnupg


class GpgError(Exception):
    pass


class GpgManager:
    def __init__(self):
        if not os.path.exists('gpghome'):
            os.mkdir('gpghome')
        self.gpg = gnupg.GPG(gnupghome='gpghome')
        self.gpg.encoding = 'utf-8'

    def list_keys(self, secret: bool = False):
        return self.gpg.list_keys(secret=secret)

    def new_key(self, name: str, email: str, ex_date: int = 0, passwd: str = None):
        no_passwd = False if passwd else True
        input_data = self.gpg.gen_key_input(key_type="RSA", key_length=2048, subkey_type='RSA', subkey_length='2048',
                                            name_real=name, name_email=email, expire_date=ex_date, passphrase=passwd,
                                            no_protection=no_passwd)
        key = self.gpg.gen_key(input_data)
        if key.status != 'ok':
            raise GpgError(key.status)

    def import_key(self, file_path: str):
        import_result = self.gpg.import_keys_file(file_path)
        if 'ok' not in import_result.results[0].keys():
            raise GpgError('Key not imported')
        self.gpg.trust_keys(import_result.results[0]['fingerprint'], 'TRUST_FULLY')

    def export_key(self, keyid: str, file_path: str, secret: bool = False):
        if secret:
            self.gpg.export_keys(keyid, secret, output=file_path, expect_passphrase=False)
        else:
            self.gpg.export_keys(keyid, output=file_path)

    def delete_key(self, fingerprint: str, private: bool = False):
        if private:
            self.gpg.delete_keys(fingerprint, private, expect_passphrase=False)
        self.gpg.delete_keys(fingerprint)
