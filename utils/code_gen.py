from random import choices
from string import ascii_letters, digits

def generate_code(length: int):
    return ''.join(choices(ascii_letters + digits, k=length))