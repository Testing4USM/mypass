class GeneratorService:
    DEFAULT_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789"

    def __init__(self, salt, max_length=16, chars=DEFAULT_CHARS) -> None:
        self.salt = salt
        self.max_length = max_length
        self.chars = chars

    def generate_password(self) -> str:
        pass