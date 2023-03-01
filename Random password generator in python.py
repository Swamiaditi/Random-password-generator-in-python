import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&?")

def random_password_generate():
    length = int(input("Enter password length: "))
    random.shuffle(characters)
    password=[]
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    print("".join(password))

random_password_generate()    