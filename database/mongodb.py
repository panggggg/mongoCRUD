import pymongo
from pymongo import results


class MongoDB:
    def __init__(self, host, port, user, password, auth_db, db, collection):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.auth_db = auth_db
        self.db = db
        self.collection = collection

    def _connect(self):
        client = pymongo.MongoClient(
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            authSource=self.auth_db,
            authMechanism="SCRAM-SHA-1",
        )
        db = client[self.db]
        self.connection = db[self.collection]

    def insert_one(self, data):
        print("[#] Save into the MongoDB")
        return self.connection.insert_one(data)

    def insert_many(self, data):
        print("[#] Save into the MongoDB")
        return self.connection.insert_many(data)

    def find(self):
        print("[#] Find all documents")
        find_result = self.connection.find({})
        print(list(find_result))
        return list(find_result)

    def find_one(self, id):
        print("[#] Find one")
        find_one = self.connection.find_one({"_id": id})
        print(find_one)
        return list(find_one)

    def update(self, id, data):
        print("[#] Update")
        result = self.connection.update({"_id": id}, {"$set": data}, upsert=True)
        print(result)
        return result

    def update_one(self, id, data):
        print("[#] Update one")
        update_one = self.connection.update_one({"_id": id}, {"$set": data})
        print(update_one)
        return update_one

    def update_many(self, pre_data, new_data):
        print("[#] Update many")
        update_many = self.connection.update_many(
            {"pre_data": pre_data}, {"$set": new_data}
        )
        return update_many

    def delete_one(self, id):
        print("[#] Delete One")
        return self.connection.delete_one({"_id": id})

    def delete_many(self, data):
        print("[#] Delete Many")
        return self.connection.delete_many(data)
