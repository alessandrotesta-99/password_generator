import base64
import random
import string


class pass_generator:
    password = 0
    letters_and_digits = string.ascii_letters + string.digits + r"""!"#$%&'()*+,-./:<=>?@[\]^_`{|}~"""

    def generate_password(self, length):
        self.password = ''.join((random.choice(self.letters_and_digits) for _ in range(length))).encode("utf-8")
        return self.encode_password(self.password)

    def encode_password(self, pwd):
        return base64.b64encode(pwd)

    def decode_password(self, pwd):
        return base64.b64decode(pwd)
