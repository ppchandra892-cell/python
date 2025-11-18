import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient("mongodb://localhost:27017/")
    db=client["db4"]
    user_col=db["users"]
    user_data=user_col.find()
    users=list(user_data)
    for user in users:
        print(user['uname'])
    
    print("document inserted")
except:
    print("unable to insert")
    
finally:
    client.close()