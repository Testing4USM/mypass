import random

class GeneratorService:
    DEFAULT_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789"

    def __init__(self, salt, max_length=25, chars=DEFAULT_CHARS) -> None:
        self.salt = salt
        self.max_length = max_length
        self.chars = chars

    def generate_password(self, length):
        length = min(length, self.max_length)
        password = ''.join(random.choice(self.chars) for _ in range(length))

        return password