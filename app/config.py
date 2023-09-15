from os import environ

MONGO_DB_USERNAME = environ.get('MONGO_DB_USERNAME')
MONGO_DB_PASSWORD = environ.get('MONGO_DB_PASSWORD')
MONGO_DB_URI = environ.get('MONGO_DB_URI')

MONGO_DB_CONNECTION_STR = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_URI}' \
                          '/?retryWrites=true&w=majority'
