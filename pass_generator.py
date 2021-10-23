import random
import string


class pass_generator:
    password = 0
    letters_and_digits = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length):
        self.password = ''.join((random.choice(self.letters_and_digits) for _ in range(length)))
        return self.password
