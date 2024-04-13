from generator import GeneratorService

def test_length_password():
    """
    Test if the generated password has the correct length.
    """
    generator = GeneratorService()
    password = generator.generate_password(10)

    assert len(password) == 10

def test_greater_max_length_password():
    """
    Test if the generated password has the correct length.
    """
    MAX_LENGTH = 16 # Default max length

    generator = GeneratorService()
    password = generator.generate_password(100)

    assert len(password) == MAX_LENGTH

def test_lower_min_length_password():
    """
    Test if the generated password has the correct length.
    """
    MIN_LENGTH = 8 # Default min length

    generator = GeneratorService()
    password = generator.generate_password(1)

    assert len(password) == MIN_LENGTH

def test_chars_password():
    """
    Test if the generated password has the correct characters.
    """
    generator = GeneratorService(chars="abc")
    password = generator.generate_password(5)

    assert any(c.isalnum() for c in password)
    assert all(c in "abc" for c in password)

def test_unicode_chars_password():
    """
    Test if the generated password has the correct unicode characters.
    """
    generator = GeneratorService(chars="🐍")
    password = generator.generate_password(5)

    assert all(c in "🐍" for c in password)