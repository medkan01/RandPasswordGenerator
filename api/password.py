"""Password generation logic for the web API."""
import random

ASCII_LB = 33  # Start from printable characters (exclude space)
ASCII_UB = 126


def random_ascii() -> str:
    """Generate a random ASCII character."""
    return chr(random.randint(ASCII_LB, ASCII_UB))


def is_number(char: str) -> bool:
    """Check if character is a digit (0-9)."""
    return 48 <= ord(char) <= 57


def is_lowercase(char: str) -> bool:
    """Check if character is a lowercase letter (a-z)."""
    return 97 <= ord(char) <= 122


def is_uppercase(char: str) -> bool:
    """Check if character is an uppercase letter (A-Z)."""
    return 65 <= ord(char) <= 90


def is_symbol(char: str) -> bool:
    """Check if character is a symbol."""
    return (33 <= ord(char) <= 126 and
            not is_number(char) and
            not is_lowercase(char) and
            not is_uppercase(char))


def generate_password(
    length: int = 12,
    lowercase: bool = True,
    uppercase: bool = False,
    numbers: bool = False,
    symbols: bool = False
) -> str:
    """
    Generate a random password with specified character types.

    Args:
        length: Password length (1-128)
        lowercase: Include lowercase letters
        uppercase: Include uppercase letters
        numbers: Include digits
        symbols: Include special characters

    Returns:
        Generated password string
    """
    if length < 1:
        length = 1
    if length > 128:
        length = 128

    # Ensure at least one character type is selected
    if not any([lowercase, uppercase, numbers, symbols]):
        lowercase = True

    password = []
    while len(password) < length:
        char = random_ascii()
        if lowercase and is_lowercase(char):
            password.append(char)
        elif uppercase and is_uppercase(char):
            password.append(char)
        elif numbers and is_number(char):
            password.append(char)
        elif symbols and is_symbol(char):
            password.append(char)

    return ''.join(password)
