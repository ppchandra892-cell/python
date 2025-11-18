import pymongo 
from pymongo import MongoClient
client=None
try:
    client=MongoClient("mongodb://localhost:27017/")
    db=client['db4']
    user_data=db['users']
    user_data.delete_many({"gender":"Male"})
    print("records sucessfully deleted")
except:
    print("undefined")
finally:
    pass
