
#safe password ganeretor for your WI-FI or anything

from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import choice

dictionary = ascii_letters + digits
pass_lenght = 8
password = ''.join(choice(dictionary) for _ in range(pass_lenght))
print(password)
