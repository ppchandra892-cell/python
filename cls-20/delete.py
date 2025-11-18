import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient("mongodb://localhost:27017/")
    db=client['db4']
    user_col=db['users']
    # no_users=user_col.count_documents({})
    user_col.delete_one({"uid":101})
    
    # print("no of users",no_users)
    print("delete sucess")
except:
    print("unable to perform")
finally:
    pass