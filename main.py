from pymongo.message import query
from database.mongodb import MongoDB
from config.development import config

mongo_config = config["mongo_config"]
print("Mongo_config : ", mongo_config)

mongo_db = MongoDB(
    mongo_config["host"],
    mongo_config["port"],
    mongo_config["user"],
    mongo_config["password"],
    mongo_config["auth_db"],
    mongo_config["db"],
    mongo_config["collection"],
)
mongo_db._connect()

#### insert one ####
# data = {
#     "_id": "0006",
#     "id": "0006",
#     "Username": "Pawornwan",
#     "Email": "p.picczy@gmail.com",
#     "Tel": "0614696233",
# }
# mongo_db.insert_one(data)


#### insert many ####
# data = [
#     {
#         "_id": "0002",
#         "id": "0002",
#         "Username": "Pangpicc",
#         "Email": "pppp@gmail.com",
#         "Tel": "0614696233",
#     },
#     {
#         "_id": "0003",
#         "id": "0003",
#         "Username": "Peeranat",
#         "Email": "peeranat9402@gmail.com",
#         "Tel": "0959243869",
#     },
#     {
#         "_id": "0004",
#         "id": "0004",
#         "Username": "BB",
#         "Email": "bbbbb@gmail.com",
#         "Tel": "0945623158",
#     },
# ]
# mongo_db.insert_many(data)


#### find ####
# mongo_db.find()


#### find one ####
# mongo_db.find_one("0002")

#### update ####
# query = "0007"
# new_data = {"Username": "Peeranat"}
# mongo_db.update(query, new_data)


#### update one ####
# query = "0007"
# new_data = {"Email": "peeranat@gmail.com", "Tel": "0959243869", "age": "22"}
# mongo_db.update_one(query, new_data)


#### update many ####
# pre_data = {"Username": "Peeranat"}
# new_data = {"Username": "Peenat"}
# mongo_db.update_many(pre_data, new_data)


#### Delete one ####
# query = "0002"
# mongo_db.delete_one(query)

#### Delete many ####
# data = {"Username": "Pawornwan"}
# mongo_db.delete_many(data)
