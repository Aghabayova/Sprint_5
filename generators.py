import random
import string


@staticmethod
def generate_random_name():
    # Generate a random name and last name.
    first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "Chris", "Laura", "David", "Emma"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Anderson"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"


@staticmethod
def generate_random_email():
    # Generate a random email address.
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@ya.ru"


@staticmethod
def generate_random_password(length=8):
    # Generate a random password.
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
