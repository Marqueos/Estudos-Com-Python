import secrets
import string


caracteres = string.ascii_letters + string.digits + string.punctuation
while True:
    senha= ''.join(secrets.choice(caracteres) for i in range(15))
    if (any(c.islower() for c in senha)
            and any(c.isupper() for c in senha)
            and sum(c.isdigit() for c in senha) >=8):
        break
print(senha)
    
"""alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break"""