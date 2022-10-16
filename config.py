DEBUG = True

USERNAME = 'postgres'
PASSWORD = 'postgres'
SERVER = 'localhost'
DB = 'carford'

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY="aplicacao_flask"