# Generate secure passwords
import random
import string

def generate_password(length):
    """ Generate a random password of length 'length' """
    password = ""
    
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)
        return password

generate_password(10)