#Extract - from Rest API
import requests,json,pymongo,csv,mysql.connector
from pymongo.errors import PyMongoError, ConnectionFailure
product_resp=requests.get('https://dummyjson.com/products')
product_data=product_resp.json()

products=product_data['products']
print(len(products))


#Transfor - based on requirement
product_json=[]    #MongoDB Collection, and json file
product_csv=[]     #CSV and Mysql Table
for product in products: 
    product_json.append({"pid":product['id'],
                         "name":product['title'],
                         "price":product['price'],
                         "category":product['category'],
                         "rating":product['rating']
                         })
    product_csv.append((product['id'],
                        product['title'],
                        product['price'],
                        product['category'],
                        product['rating']
                        ))

#print(product_json)
#Load     - into JSON,MongoDB,CSV,Mysql Table
#JSON and MongoDB -Collection
fp2=open("products.json",'w')
json.dump(product_json,fp2)
print("New JSON File created")


#Load int csv file 
fp1=open('product.csv','w',newline="")
cw_obj=csv.writer(fp1)
cw_obj.writerow(["pid","name","price","caterogy","rating"])
cw_obj.writerows(product_csv)
print("New CSV File Created!")


try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['db2']
    product_col=db['products']
    product_col.insert_many(product_json)
    print("Product Document inseted successfully")
except ConnectionError as err:
    print(err)
except PyMongoError as err:
    print(err)

#load into mysql Product tables
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="db2"
                                  ) 
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
            insert into products(pid,name,price,category,rating) values(%s,%s,%s,%s,%s);
            '''
    cursor.executemany(sql_st,product_csv)
    dbcon.commit()
    print("Data inserted into Mysql Table!GN")
except:
    pass 