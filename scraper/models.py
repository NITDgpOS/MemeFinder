import pymongo

dbClient = pymongo.MongoClient('mongodb+srv://jayv:simplepass@cluster0-ei4tu.mongodb.net/test?retryWrites=true')
dbc = dbClient['MemeFinder']


def db(table_name):
    return getattr(dbc, table_name)


def dropCollection(table_name):
    dbc.drop_collection(table_name)


def closeConnection():
    dbc.close()
