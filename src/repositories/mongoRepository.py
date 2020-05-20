from src.modules.conexao_mongodb.ConexaoMongo import conexao

banco = 'inss'

def count_documents(collection,arg):
    try:
        return conexao(banco).get_collection(collection).count_documents(arg)
    except Exception as e:
        raise Exception('Falha Mongo: ' + find.__name__ + ' - ' + e.__str__())

def find(collection,arg,**order):
    try:
        return conexao(banco).get_collection(collection).find(arg).sort(order['field'],order['direction'])
    except Exception as e:
        raise Exception('Falha Mongo: ' + find.__name__ + ' - ' + e.__str__())


def findOne(collection,filter):
    try:
        return conexao(banco).get_collection(collection).find_one(filter)
    except Exception as e:
        raise Exception('Falha Mongo: ' + findOne.__name__ + ' - ' + e.__str__())


def insertOne(collection,obj):
    try:
        return conexao(banco).get_collection(collection).insert_one(obj)
    except Exception as e:
        raise Exception('Falha Mongo: ' + insertOne.__name__ + ' - ' + e.__str__())


def updateOne(collection,obj,filter = None):
    try:

        if not filter:
            filter = {'_id': obj['_id']}

        return conexao(banco).get_collection(collection).update_one(filter,obj,upsert=True)
    except Exception as e:
        raise Exception('Falha Mongo: ' + updateOne.__name__ + ' - ' + e.__str__())

def findOneAndUpdate(collection,filter,obj):
    try:
        return conexao(banco).get_collection(collection).find_one_and_update(filter,obj,upsert=True)
    except Exception as e:
        raise Exception('Falha Mongo: ' + findOneAndUpdate.__name__ + ' - ' + e.__str__())



def findOneAndReplace(collection,filter,obj):
    try:
        return conexao(banco).get_collection(collection).find_one_and_replace(filter,obj,upsert=True)
    except Exception as e:
        raise Exception('Falha Mongo: ' + findOneAndReplace.__name__ + ' - ' + e.__str__())



def findOneAndDelete(collection,filter):
    try:
        return conexao(banco).get_collection(collection).find_one_and_delete(filter)
    except Exception as e:
        raise Exception('Falha Mongo: ' + findOneAndDelete.__name__ + ' - ' + e.__str__())




def deletetOne(collection,filter):
    try:
        return conexao(banco).get_collection(collection).delete_one(filter)
    except Exception as e:
        raise Exception('Falha Mongo: ' + deletetOne.__name__ + ' - ' + e.__str__())


def insertManyOnlyNew(collection, objs):
    try:

        for obj in objs:

            filter = { '_id' : obj['_id']}

            match = findOne(collection,filter)

            if not match:
                insertOne(collection,obj)


    except Exception as e:
        raise Exception('Falha Mongo: ' + insertManyOnlyNew.__name__ + ' - ' + e.__str__())



def view(collection, view,order=1):
    try:

        if view == 'importar':

            arg = {"error":{"$exists": False}, "evento_julgado": '' }
            return find(collection,arg).sort("_id", order)

        elif view == 'com_erros':

            arg = {"error": True}
            return find(collection, arg)

    except Exception as e:
        raise Exception('Falha Mongo: ' + view.__name__ + ' - ' + e.__str__())
