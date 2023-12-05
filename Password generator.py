import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Usage example:
password_length = 8  # Change this to set the desired length of the password
new_password = generate_password(password_length)
print("Generated Password:", new_password)