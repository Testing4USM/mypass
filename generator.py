import random
import string

class GeneratorService:
    """
    A service that generates random passwords.
    """
    DEFAULT_CHARS = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits
    )

    def __init__(self, min_length=8, max_length=16, chars=DEFAULT_CHARS) -> None:
        if not chars.isascii():
            raise ValueError("Chars must be ASCII")

        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def generate_password(self, length):
        """
        Generates a random password of the specified length.
        """
        if length > self.max_length:
            length = self.max_length

        length = max(length, self.min_length)
        password = ''.join(random.choice(self.chars) for _ in range(length))

        return password