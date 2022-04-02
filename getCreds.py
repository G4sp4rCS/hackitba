import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def mailCredentials():

    mail = os.getenv('MAIL')
    password = os.getenv('PASSWORD')
    return mail, password