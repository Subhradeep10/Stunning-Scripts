import secrets
import string

# The source from which the password is generated
source = string.ascii_letters + string.digits + string.punctuation
length = 12  # length of the generated password

while True:
    password = ''
    for i in range(length):
        password += ''.join(secrets.choice(source))
    # Checks if the generated password contains atleast one special character and an upper case character
    if (any(char in string.punctuation for char in password) and 
        any(char in string.ascii_uppercase for char in password)):
            break
print(password)