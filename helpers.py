import random
from faker import Faker

fake = Faker()


def login():
    user_login = fake.name()
    return user_login


def password():
    user_password = random.randrange(100000, 999999)
    return user_password
