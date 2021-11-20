import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('USER')
password = os.getenv('KEY')

print('Логин - {}\nПароль - {}'.format(login, password))
