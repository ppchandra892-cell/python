#Extract - from Rest API
import requests,json,pymongo,csv,mysql.connector
from pymongo import MongoClient
from pymongo.errors import PyMongoError, ConnectionFailure
product_resp=requests.get('https://dummyjson.com/products')
product_data=product_resp.json()

products=product_data['products']
print(len(products))
#transform
product_json=[]
product_csv=[]
for product in products:
    product_json.append({"id":product['id'],
                         "price":product['price'],
                         "name":product['title'],
                         "category":product['category'],
                         "rating":product['rating']
                        })
    product_csv.append((product['id'],
                        product['price'],
                        product['title'],
                        product['rating']))
    
#loadjson
fp2=open("pro.json",'w')
json.dump(product_json,fp2)
print("new json created")
#loadcsv
fp1=open("pro.csv",'w')
cw=csv.writer(fp1)
cw.writerow(["id","price","title","rating"])
cw.writerows(product_csv)
print("new csv created")
try:
    client=MongoClient("mongodb://localhost:27017/")
    db=client["db4"]
    user_col=db["products"]
    user_col.insert_many(products)
    user_col.insertmany(product_json)
except:
    pass
finally:
    pass
#load the data into mysql
dbcon=None
cursor=None
dbcon=mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="db4"
                                  ) 
    # print(dbcon.is_connected())
cursor=dbcon.cursor()
sql_st='''
            insert into pro(id,price,title,category,rating) values(%s,%s,%s,%s,%s);
            '''
print("after connection")

cursor.executemany(sql_st,product_csv)
print("before connection")
dbcon.commit()
print("Data inserted into Mysql Table!GN")
cursor.close()
dbcon.close()
    

    