import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient("mongodb://localhost:27017/")
    db=client["db4"]
    user_col=db["users"]
    users=[{"uid":1,"uname":"Salvatore","gender":"Enoksson"},
{"uid":2,"uname":"Rosella","gender":"Wakeling"},
{"uid":3,"uname":"Jodi","gender":"Bamforth"},
{"uid":4,"uname":"Ilyssa","gender":"Hansen"},
{"uid":5,"uname":"Hendrik","gender":"Brusby"},
{"uid":6,"uname":"Randolph","gender":"Redpath"},
{"uid":7,"uname":"Lennie","gender":"Brettor"},
{"uid":8,"uname":"Joellen","gender":"Frango"},
{"uid":9,"uname":"Englebert","gender":"Brunroth"},
{"uid":10,"uname":"Conney","gender":"De Marchi"},
{"uid":11,"uname":"Ramsey","gender":"Swanwick"},
{"uid":12,"uname":"Darlleen","gender":"Geeson"},
{"uid":13,"uname":"Darwin","gender":"Grayne"},
{"uid":14,"uname":"Wallas","gender":"Trowel"},
{"uid":15,"uname":"Babbie","gender":"Cotesford"},
{"uid":16,"uname":"Cynthy","gender":"Bountiff"},
{"uid":17,"uname":"Bailey","gender":"Henrie"},
{"uid":18,"uname":"Wilma","gender":"Gethin"},
{"uid":19,"uname":"Teirtza","gender":"Laneham"},
{"uid":20,"uname":"Harold","gender":"Kift"},
{"uid":21,"uname":"Cherin","gender":"Haburne"},
{"uid":22,"uname":"Fitz","gender":"Turnell"},
{"uid":23,"uname":"Cirilo","gender":"Pavelin"},
{"uid":24,"uname":"Adrea","gender":"Izkovitz"},
{"uid":25,"uname":"Rivkah","gender":"Ludvigsen"},
{"uid":26,"uname":"Lilllie","gender":"Spoure"},
{"uid":27,"uname":"Kalila","gender":"Lamps"},
{"uid":28,"uname":"Nina","gender":"Graeser"},
{"uid":29,"uname":"Taite","gender":"Boxill"},
{"uid":30,"uname":"Dov","gender":"Hinder"},
{"uid":31,"uname":"Barrie","gender":"Ollier"},
{"uid":32,"uname":"Janka","gender":"Nannizzi"},
{"uid":33,"uname":"Graehme","gender":"Malkinson"},
{"uid":34,"uname":"Calli","gender":"Mallebone"},
{"uid":35,"uname":"Olly","gender":"Mackro"},
{"uid":36,"uname":"Armando","gender":"Minnock"},
{"uid":37,"uname":"Vachel","gender":"Gosland"},
{"uid":38,"uname":"Karmen","gender":"Arch"},
{"uid":39,"uname":"Jacquelynn","gender":"Worster"},
{"uid":40,"uname":"Simmonds","gender":"Holbarrow"},
{"uid":41,"uname":"Chelsey","gender":"Pellissier"},
{"uid":42,"uname":"Norry","gender":"Busch"},
{"uid":43,"uname":"Gae","gender":"Bruhnicke"},
{"uid":44,"uname":"Jamie","gender":"McElrea"},
{"uid":45,"uname":"Arlan","gender":"Camerana"},
{"uid":46,"uname":"Brennen","gender":"Gockeler"},
{"uid":47,"uname":"Ardenia","gender":"Jancey"},
{"uid":48,"uname":"Cleve","gender":"Axelby"},
{"uid":49,"uname":"Cory","gender":"Royce"},
{"uid":50,"uname":"Ervin","gender":"Dunstan"}]
    # user_col.insert_one({"uid":101,"uname":"rahul"})
    user_col.insert_many(users)
    print("document inserted")
except:
    print("unable to insert")
    
finally:
    client.close()