import pandas as pd
import requests, json
import mysql.connector as me

product_resp=requests.get('https://dummyjson.com/products')
product_data=product_resp.json()

products=product_data['products']

li = []

# print(products[0])
for i in products:
    payload ={
        "id": i["id"],
        "title":i["title"]
    }
    li.append(payload)

db=me.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="db4"
                                  ) 
cur = db.cursor()
count = 0
for i in li:
    cur.execute("insert into mypro values(%s,%s)",(i["id"], i["title"]))
    db.commit()
    count +=1
    print(f"record {count} insert")
cur.close()
db.close()