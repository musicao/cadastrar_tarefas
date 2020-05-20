from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import urllib.parse

def conexao(database):
    try:

        MONGO_INITDB_ROOT_USERNAME = "user"
        MONGO_INITDB_ROOT_PASSWORD = "12345678"


        client = MongoClient('mongodb://%s:%s@127.0.0.1' % (MONGO_INITDB_ROOT_USERNAME,
                                                                         MONGO_INITDB_ROOT_PASSWORD), 27107)

        client.admin.command('ismaster')
        return client[database]

    except ConnectionFailure:
        raise Exception("Server not available")

